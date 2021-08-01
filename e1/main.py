import uvicorn
import socketio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
sio = socketio.AsyncServer(async_mode="asgi", logger=True)

sio_asgi_app = socketio.ASGIApp(sio, app, socketio_path="/socket.io")
app.mount("/socket.io", sio_asgi_app)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="./static"), name="static")


@sio.event
def connect(data):
    print(data)
    pass


@sio.event(namespace="/chattings")
def new_user(data):
    print("fuckfuckfuck")
    print(data)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request, "title": "fastapi realtime chatting room"}
    return templates.TemplateResponse("index.html", context=context)


if __name__ == "__main__":
    uvicorn.run("main:sio_asgi_app", host="localhost", port=8080, reload=True)
