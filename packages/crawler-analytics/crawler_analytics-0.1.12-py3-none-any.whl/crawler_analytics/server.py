import json
import argparse
from aiohttp import web
from main import Analytics


parser = argparse.ArgumentParser()
parser.add_argument(
    "project_name",
    metavar="Project Name",
    type=str,
    help="Project Name",
)
parser.add_argument(
    "--port",
    default=8080,
    metavar="Server Port",
    type=int,
)
args = parser.parse_args()
analytics = Analytics(project_name=args.project_name)


async def handle(request):
    return web.Response(
        text=json.dumps(await analytics.data(), indent=4),
        content_type="application/json",
    )


def server():
    app = web.Application()
    app.router.add_get("/", handle)

    web.run_app(app, host="localhost", port=args.port)


if __name__ == "__main__":
    server()
