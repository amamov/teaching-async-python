from odmantic import Model


class PhotoModel(Model):
    username: str
    message: str

    class Config:
        collection = "photos"
