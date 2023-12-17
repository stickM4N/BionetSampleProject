from abc import ABC, abstractmethod
from typing import Callable

from application.requests.core.base_request import BaseRequest


class BaseRequestHandler(ABC):
    _request_type: type[BaseRequest] = None

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
    def validate_handle(handle: Callable) -> Callable:
        async def wrapper(self, request: BaseRequest):
            assert isinstance(request, self.request_type), \
                f'request is not an instance of {self.request_type.__name__}'

            result = await handle(self, request)

            assert isinstance(result, self.result_type), \
                f'result is not an instance of {self.result_type.__name__}'

            return result

        return wrapper

    @abstractmethod
    async def handle(self, request: BaseRequest) -> result_type:
        assert isinstance(request, BaseRequest), 'request must be an instance of BaseRequest'
