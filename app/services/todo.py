from app.models.todo import TodoModel
from app.models import mongodb


async def get_all():
    return await mongodb.engine.find(TodoModel)


async def create_todo(todo: TodoModel):
    return await mongodb.engine.save(todo)
