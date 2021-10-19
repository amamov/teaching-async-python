from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb
from app.models.book import BookModel
from app.book_scraper import NaverBookScraper

BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # book = BookModel(keyword="파이썬", publisher="BJPublic", price=1200, image="me.png", hhh="askljdlkas")
    # print(await mongodb.engine.save(book))  # DB에 저장
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이"},
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    # 1. 쿼리에서 검색어 추출
    keyword = q
    # (예외처리)
    #  - 검색어가 없다면 사용자에게 검색을 요구 return
    #  - 해당 검색어에 대해 수집된 데이터가 이미 DB에 존재한다면 해당 데이터를 사용자에게 보여준다. return
    # 2. 데이터 수집기로 해당 검색어에 대해 데이터를 수집한다.
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
    # 3. DB에 수집된 데이터를 저장한다.
    await mongodb.engine.save_all(book_models)

    #  - 수집된 각각의 데이터에 대해서 DB에 들어갈 모델 인스턴스를 찍는다.
    #  - 각 모델 인스턴스를 DB에 저장한다.
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이"},
    )


@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    """after app shutdown"""
    mongodb.close()
