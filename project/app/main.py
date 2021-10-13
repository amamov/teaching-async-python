from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이"},
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, s: str):
    # print(q)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이"},
    )
