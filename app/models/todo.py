from odmantic import Model


class TodoModel(Model):
    username: str
    message: str

    class Config:
        collection = "todolist"
