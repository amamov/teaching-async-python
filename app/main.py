from starlette.middleware.gzip import GZipMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import routers
from app.config import BASE_DIR
from app.models import mongodb


app = FastAPI(title="데이터 수집가", version="0.0.1")
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.mount("/static", StaticFiles(directory=BASE_DIR / "statics"), name="static")


app.include_router(routers.root.router, prefix="", tags=["ROOT"])
app.include_router(routers.todolist.router, prefix="/api/todolist", tags=["API_TODOLIST"])


@app.on_event("startup")
async def on_app_start():
    """
    before app starts
    """
    await mongodb.connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    """
    after app shutdown
    """
    await mongodb.close()
