import os
import time
from redis import asyncio as aioredis
from nanoid import generate

from datetime import datetime
SPLITTER = ":"

KEYS = {
    "crawler": "crawler",
    "status": "status",
    "count": {
        "_date": "count:date",
        "total": "count:total",
        "target": "count:target",
    },
    "node": "node",
    "images": "images",
}

def get_date_str():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y%m%d')
    return formatted_date

class Analytics:
    def __init__(self, _redis: aioredis.Redis = None, project_name: str = None):
        self.project_name = project_name.lower() if project_name else None
        self.r = (
            aioredis.Redis.from_url(
                url=os.environ.get("REDIS_URL"), decode_responses=True
            )
            if _redis is None
            else _redis
        )
        self.is_init = False

    async def init(self):
        await self.r.sadd(KEYS["crawler"], self.project_name)

    def _key(self, key):
        """Prefix the key with the project name if it exists."""
        return f"{self.project_name}{SPLITTER}{key}" if self.project_name else key

    async def _count_nodes(self):
        node_key_pattern = self._key(KEYS["node"]) + "*"
        count = 0
        async for _ in self.r.scan_iter(match=node_key_pattern):
            count += 1
        return count

    async def data(self):
        status_key = self._key(KEYS["status"])
        return {
            "name": self.project_name if self.project_name else "default",
            "status": await self.r.get(status_key),
            "count": {
                "total": await self.r.get(self._key(KEYS["count"]["total"])),
                "target": await self.r.get(self._key(KEYS["count"]["target"])),
                "node": await self._count_nodes(),
                "today": await self._get_today(),
                "yesterday": await self._get_yesterday(),
            },
        }

    async def set_target(self, n: int):
        target_key = self._key(KEYS["count"]["target"])
        await self.r.set(target_key, n)

    async def _get_today(self):
        return await self._get_image_count(start_time=int(time.time()) - 86400)

    async def _get_yesterday(self):
        return await self._get_image_count(start_time=int(time.time()) - 172800)

    async def _get_image_count(self, start_time: int = None):
        """先删除超过保留期限的数据，再查询"""
        current_time = time.time()
        end_time = current_time - 259200  # 三天
        await self.r.zremrangebyscore(self._key(KEYS["images"]), min=0, max=end_time)

        start_time = start_time if start_time else time.time() - 86400
        return await self.r.zcount(
            self._key(KEYS["images"]), min=start_time, max=current_time
        )

    async def success(self, image_count: int = 1, image_pks: list = None, verbose=False):
        if not self.is_init:
            await self.init()
            self.is_init = True
        score = time.time()
        if verbose:
            if image_pks:
                image_count = len(image_pks) if image_pks else image_count
                z = {image_pks[i]: score for i in range(image_count)}
            else:
                z = {generate(): score for _ in range(image_count)}

            await self.r.zadd(self._key(KEYS["images"]), z)

        total_key = self._key(KEYS["count"]["total"])
        await self.r.incrby(total_key, image_count)
        key = self._key(KEYS["count"]["date"]+SPLITTER+get_date_str())
        await self.r.incrby(key, image_count)
