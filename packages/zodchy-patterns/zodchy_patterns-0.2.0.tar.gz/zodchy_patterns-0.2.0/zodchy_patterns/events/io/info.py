import collections.abc
import dataclasses

from .generic import HttpEvent


@dataclasses.dataclass
class HttpInfo(HttpEvent):
    pass


@dataclasses.dataclass
class HttpCreatedInfo(HttpInfo):
    def get_content(self) -> dict:
        data = dataclasses.asdict(self)
        return {'data': data} if data else None

    def get_status_code(self):
        return 200 if self.get_content() else 201


@dataclasses.dataclass
class HttpItemInfo(HttpInfo):
    data: collections.abc.Mapping

    def get_content(self):
        return {'data': self.data} if self.data else None

    def get_status_code(self):
        return 200 if self.data else 404


@dataclasses.dataclass
class HttpListInfo(HttpInfo):
    data: collections.abc.Iterable[collections.abc.Mapping]

    def get_content(self):
        return {
            'data': self.data or []
        }


@dataclasses.dataclass
class HttpPaginatedListInfo(HttpListInfo):
    total: int

    def get_content(self):
        return super().get_content() | {
            'pagination': {
                'quantity': self.total
            }
        }
