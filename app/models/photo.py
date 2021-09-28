from odmantic import Model


class PhotoModel(Model):
    keyword: str
    image_src: str

    class Config:
        collection = "photos"
