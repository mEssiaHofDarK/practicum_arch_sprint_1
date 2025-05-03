import random
from aiohttp import web


async def tmp(request):
    temp = (random.randint(100, 900))/10
    return web.Response(text=str(temp))


app = web.Application()
app.add_routes([web.get("/temperature", tmp)])


if __name__ == "__main__":
    web.run_app(app)
