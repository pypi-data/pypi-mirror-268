import re
import dataclasses
from zodchy import codex

from . import generic


@dataclasses.dataclass
class HttpError(generic.HttpEvent, codex.Error):
    code: int = 500
    message: str | None = None
    details: dict | None = None

    def get_content(self) -> dict:
        details = self.details or {}
        for field in dataclasses.fields(self):
            if field.name not in ('code', 'message', 'details'):
                details[field.name] = getattr(self, field.name)
        return {
            'data': {
                'code': self.code,
                'message': self._get_message(),
                'details': details or None
            }
        }

    def get_status_code(self) -> int:
        return self.code

    def _get_message(self):
        if self.message is None:
            matches = re.finditer(
                '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)',
                type(self).__name__
            )
            return " ".join((_[0] for _ in matches))
        return self.message


@dataclasses.dataclass
class HttpClientError(HttpError):
    code: int = 400

    def get_status_code(self) -> int:
        return self.code


@dataclasses.dataclass
class HttpAuthError(HttpClientError):
    code: int = 403


@dataclasses.dataclass
class HttpRateLimitError(HttpClientError):
    code: int = 429


@dataclasses.dataclass
class HttpValidationError(HttpClientError):
    code: int = 422


@dataclasses.dataclass
class HttpNotFoundError(HttpClientError):
    code: int = 404


@dataclasses.dataclass
class HttpDuplicationError(HttpClientError):
    code: int = 409


@dataclasses.dataclass
class HttpEmptyRosterError(HttpClientError):
    code: int = 200

    def get_content(self) -> dict:
        return {'data': []}
