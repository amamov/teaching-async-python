from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.config import get_secret


class __MongoDB:

    MONGO_URL = get_secret("MONGO_URL")
    MONGO_DB_NAME = get_secret("MONGO_DB_NAME")
    MONGO_MAX_CONNECTIONS = get_secret("MONGO_MAX_CONNECTIONS", "10")
    MONGO_MIN_CONNECTIONS = get_secret("MONGO_MIN_CONNECTIONS", "10")

    def __init__(self) -> None:
        self.__client: AsyncIOMotorClient = None
        self.__engine: AIOEngine = None

    @property
    def client(self) -> AsyncIOMotorClient:
        return self.__client

    @property
    def engine(self) -> AIOEngine:
        return self.__engine

    async def connect(self):
        """
        Connect to MongoDB
        """
        self.__client = AsyncIOMotorClient(
            self.MONGO_URL,
            maxPoolSize=self.MONGO_MAX_CONNECTIONS,
            minPoolSize=self.MONGO_MIN_CONNECTIONS,
        )
        self.__engine: AIOEngine = AIOEngine(
            motor_client=self.__client, database=self.MONGO_DB_NAME
        )

    async def close(self):
        """
        Close MongoDB Connection
        """
        self.__client.close()


mongodb = __MongoDB()
