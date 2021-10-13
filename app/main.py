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
    keyword = request.query_params.get("q")  # 쿼리에서 키워드 추출
    if not keyword:  # 키워드가 없다면 사용자에게 검색을 요구
        context = {"request": request}
        return templates.TemplateResponse("index.html", context=context)
    if await mongodb.engine.find_one(BookModel, BookModel.keyword == keyword):
        # 키워드에 대해 수집된 데이터가 DB에 존재한다면 해당 데이터를 사용자에게 보여준다.
        books = await mongodb.engine.find(BookModel, BookModel.keyword == keyword)
        context = {"request": request, "keyword": keyword, "books": books}
        return templates.TemplateResponse("index.html", context=context)
    naver_book_scraper = NaverBookScraper()  # 수집기 인스턴스
    books = await naver_book_scraper.search(keyword, 10)  # 데이터 수집
    book_models = []
    for book in books:  # 수집된 각각의 데이터에 대해서 DB에 들어갈 모델 인스턴스를 찍는다.
        book_model = BookModel(
            keyword=keyword,
            publisher=book["publisher"],
            price=book["price"],
            image=book["image"],
        )
        book_models.append(book_model)
    await mongodb.engine.save_all(book_models)  # 각 모델 인스턴스를 DB에 저장한다.
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
