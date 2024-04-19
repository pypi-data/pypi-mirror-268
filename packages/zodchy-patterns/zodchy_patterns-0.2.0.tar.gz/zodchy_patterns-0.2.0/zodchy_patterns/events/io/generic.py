import dataclasses
from zodchy import codex


@dataclasses.dataclass
class HttpEvent(codex.ResponseEvent):
    def get_content(self) -> dict:
        data = dataclasses.asdict(self)
        return {
            'data': data or None
        }

    @staticmethod
    def get_status_code() -> int:
        return 200
