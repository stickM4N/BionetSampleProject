from dataclasses import asdict
from typing import final

from aredis_om import RedisModel, NotFoundError, HashModel, JsonModel

from infrastructure.repositories.core.base_repository import BaseRepository


class RedisRepository(BaseRepository):
    _model_type: type[object]

    def __init__(self, use_json_model_instead_of_hash_model: bool = False):
        self._base_entity_type = JsonModel if use_json_model_instead_of_hash_model else HashModel

        super().__init__()

    @final
    async def create(self, entity) -> RedisModel:
        entity = self._entity_type(**asdict(entity))
        await entity.save()

        return entity

    @final
    async def find_by_key(self, key: str) -> RedisModel | None:
        try:
            return await self._entity_type.get(key)

        except NotFoundError:
            return None

    @final
    async def update(self, key: str, **fields) -> RedisModel | None:
        try:
            entity_in_db = await self._entity_type.get(key)
            await entity_in_db.update(**fields)
            await entity_in_db.save()

            return entity_in_db

        except NotFoundError:
            return None

    @final
    async def delete_by_key(self, key: str) -> None:
        await self._entity_type.delete(key)

    @final
    async def set_expiration_by_key(self, key: str, seconds: int) -> None:
        try:
            entity_in_db = await self._entity_type.get(key)
            await entity_in_db.expire(seconds)

        except NotFoundError:
            return None
