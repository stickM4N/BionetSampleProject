from abc import ABC
from types import NoneType


class BaseRequest(ABC):
    _result_type: type[object | NoneType] = None

    def __init__(self):
        assert self._result_type is not None, '_result_type field is required'

    @property
    def result_type(self) -> type:
        return self._result_type
