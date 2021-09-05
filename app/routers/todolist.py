from fastapi import APIRouter
import app.services.todo as todo_service
from app.models.todo import TodoModel


router = APIRouter()


@router.get("/")
async def get_all_todo():
    return await todo_service.get_all()


@router.post("/")
async def post_todo(todo: TodoModel):
    return await todo_service.create_todo(todo)
