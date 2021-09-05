from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.config import BASE_DIR
from app.scrapers import photo_scraper

router = APIRouter()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "title": "데이터 수집가"}
    return templates.TemplateResponse("index.html", context=context)


@router.get("/search", response_class=HTMLResponse)
async def search_result(request: Request):
    print(request)
    print(request.query_params)
    print(request.query_params.get("q"))
    keyword = request.query_params.get("q")
    result = await photo_scraper.search(keyword, 50)
    context = {"request": request, "keyword": keyword, "result": result}
    return templates.TemplateResponse("index.html", context=context)
