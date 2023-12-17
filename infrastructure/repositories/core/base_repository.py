from abc import ABC, abstractmethod
from dataclasses import is_dataclass


class BaseRepository(ABC):
    _model_type: type[object] = None
    _base_entity_type: type[object] = None

    def __init__(self):
        assert self._model_type is not None, '_model_type field is required'
        assert is_dataclass(self._model_type) and isinstance(self._model_type, type), \
            '_model_type field must be a dataclass type'

        assert self._base_entity_type is not None, '_base_entity_type field is required'

        class Entity(self._base_entity_type, self._model_type):
            pass

        self._entity_type = Entity

    @property
    def model_type(self) -> type:
        return self._model_type

    @abstractmethod
    async def create(self, **fields) -> object:
        ...

    @abstractmethod
    async def find_by_key(self, key: int | str) -> object | None:
        ...

    @abstractmethod
    async def update(self, key: int | str, **fields) -> object | None:
        ...

    @abstractmethod
    async def delete_by_key(self, key: int | str) -> object | None:
        ...
