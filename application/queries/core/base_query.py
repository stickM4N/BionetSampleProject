from types import NoneType

from application.request_handlers.core.base_request import BaseRequest


class BaseQuery(BaseRequest):

    def __init__(self):
        super().__init__()

        assert self._result_type is not NoneType, 'BaseQuery is designed to return data. Use BaseCommand instead'
