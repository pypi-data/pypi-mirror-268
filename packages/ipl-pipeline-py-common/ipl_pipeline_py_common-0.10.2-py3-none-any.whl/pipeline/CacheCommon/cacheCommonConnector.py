from redis import asyncio as aioredis
from typing import Optional, Union, Type, TypeVar, List
import json

from pipeline.exceptions import NoConnectionError

T = TypeVar('T')


class CacheCommonConnector:
    """
    Common Cache Connector for Redis
    """
    def __init__(self, redis_uri: str):
        """
        Constructor
        :param redis_uri: Redis Connection URI
        """
        self._redis_uri = redis_uri
        self._redis_client: Optional[aioredis.Redis] = None

    async def connect(self):
        """Create database connection."""
        self._redis_client = await aioredis.from_url(self._redis_uri)

    async def disconnect(self):
        """Close database connection."""
        if self._redis_client:
            await self._redis_client.close()

    async def set_key(self, key: str, value: Union[dict, list, str], expire: Union[int, None] = 1800) -> bool:
        """
        Add Key:Value to Redis cache
        :param key: Key name
        :param value: Value Data dict
        :param expire: expiry time in seconds, default 1800s
        :return: if operation was successful
        """
        if isinstance(value, str):
            cache_str = value
        else:
            cache_str = json.dumps(value)
        if self._redis_client is None:
            raise NoConnectionError("Redis client not connected")
        async with self._redis_client.client() as conn:
            if expire and expire > 0:
                ok = await conn.execute_command("SET", f"{key}", cache_str, "EX", f"{expire}")
            else:
                ok = await conn.execute_command("SET", f"{key}", cache_str)
            return bool(ok)

    async def get_key(self, key: str, instance_type: Type[T]) -> Optional[T]:
        """
        Retrieve value via key from Redis cache
        :param instance_type:
        :param key: Key to retrieve data from
        :return: None or dict
        """
        if self._redis_client is None:
            raise NoConnectionError("Redis client not connected")
        if data := await self._redis_client.get(f"{key}"):
            loaded_data = json.loads(data)
            return instance_type(**loaded_data)
        return None

    async def delete_keys(self, key: List[str]) -> bool:
        """
        Delete key from Redis Cache
        :param key: Key Name
        :return: if operation was successful
        """
        if self._redis_client is None:
            raise NoConnectionError("Redis client not connected")
        if await self._redis_client.delete(*key):
            return True
        else:
            return False

