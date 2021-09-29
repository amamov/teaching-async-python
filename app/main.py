from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.book_scraper import NaverBookScraper
from app.config import BASE_DIR
from app.models import mongodb
from app.models.book import BookModel


app = FastAPI(title="데이터 수집가", version="0.0.1")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "title": "데이터 수집가"}
    return templates.TemplateResponse("index.html", context=context)


@app.get("/search", response_class=HTMLResponse)
async def search_result(request: Request):
    keyword = request.query_params.get("q")
    if not keyword:
        context = {"request": request}
        return templates.TemplateResponse("index.html", context=context)
    if await mongodb.engine.find_one(BookModel, BookModel.keyword == keyword):
        books = await mongodb.engine.find(BookModel, BookModel.keyword == keyword)
        context = {"request": request, "keyword": keyword, "books": books}
        return templates.TemplateResponse("index.html", context=context)
    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword, 10)
    book_models = []
    for book in books:
        book_model = BookModel(
            keyword=keyword,
            publisher=book["publisher"],
            price=book["price"],
            image=book["image"],
        )
        book_models.append(book_model)
    await mongodb.engine.save_all(book_models)
    context = {"request": request, "keyword": keyword, "books": books}
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
