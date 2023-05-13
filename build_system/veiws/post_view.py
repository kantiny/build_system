from aiohttp import web

from main import app
from build_system.utils import handle_json_error


@app.router.post("/get_tasks")
@handle_json_error
async def get_tasks(request: web.Request) -> web.Response:
    post = await request.json()
    input_json = post["input_json"]

    return web.json_response(
        {
            "status": "ok",
            "data": input_json,
        }
    )
