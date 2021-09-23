from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.config import BASE_DIR
from app.models import mongodb
from app.scrapers import photo_scraper


app = FastAPI(title="데이터 수집가", version="0.0.1")
app.mount("/statics", StaticFiles(directory=BASE_DIR / "statics"), name="static")


templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "title": "데이터 수집가"}
    return templates.TemplateResponse("index.html", context=context)


@app.get("/search", response_class=HTMLResponse)
async def search_result(request: Request):
    # print(request)
    # print(request.query_params)
    # print(request.query_params.get("q"))
    keyword = request.query_params.get("q")
    result = await photo_scraper.search(keyword, 50)
    context = {"request": request, "keyword": keyword, "result": result}
    return templates.TemplateResponse("index.html", context=context)


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
