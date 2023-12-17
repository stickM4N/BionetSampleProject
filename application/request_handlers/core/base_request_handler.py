from abc import ABC, abstractmethod
from types import NoneType
from typing import Callable

from application.requests.core.base_request import BaseRequest


class BaseRequestHandler(ABC):
    _request_type: type[BaseRequest, NoneType] = None

    def __init__(self):
        assert self._request_type is not None, '_request_type field is required'
        assert issubclass(self._request_type, BaseRequest), '_request_type must be a subclass of BaseRequest'

    @property
    def request_type(self) -> type:
        return self._request_type

    @property
    def result_type(self) -> type:
        return self._request_type.result_type.fget(self._request_type)

    @staticmethod
    def assert_return(handle: Callable) -> Callable:
        async def wrapper(self, request: BaseRequest):
            assert request.result_type == self.result_type, \
                f'Handle return value is not an instance of {self.result_type.__name__}'

            return await handle(self, request)

        return wrapper

    @abstractmethod
    async def handle(self, request: BaseRequest) -> result_type:
        assert isinstance(request, BaseRequest), 'request must be an instance of BaseRequest'
