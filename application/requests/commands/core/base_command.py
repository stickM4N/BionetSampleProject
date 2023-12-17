from types import NoneType

from application.requests.core.base_request import BaseRequest


class BaseCommand(BaseRequest):

    def __init__(self):
        super().__init__()

        assert self._result_type is NoneType, 'BaseCommand is not designed to return data. Use BaseQuery instead'
