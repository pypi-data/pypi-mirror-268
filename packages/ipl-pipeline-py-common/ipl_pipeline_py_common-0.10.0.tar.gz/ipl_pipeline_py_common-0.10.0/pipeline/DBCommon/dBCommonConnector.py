import motor.motor_asyncio
from typing import Optional
from pipeline.exceptions import NoConnectionError


class DBCommonConnector:
    """
    Common DB Connector for MongoDB
    """

    def __init__(self, mongo_uri: str, db_name: str, ):
        """
        Constructor
        :param mongo_uri: MongoDB Connection URI
        :param db_name: DB Name
        """
        self._mongo_uri = mongo_uri
        self._db_name = db_name
        self._mongo_client: Optional[motor.motor_asyncio.AsyncIOMotorClient] = None
        self._db: Optional[motor.motor_asyncio.AsyncIOMotorDatabase] = None

    async def connect(self):
        """Create database connection."""
        self._mongo_client = motor.motor_asyncio.AsyncIOMotorClient(self._mongo_uri, tz_aware=True)
        self._db = self._mongo_client[self._db_name]

    async def disconnect(self):
        """Close database connection."""
        if self._mongo_client:
            self._mongo_client.close()
        else:
            raise NoConnectionError("MongoDB client not connected")
