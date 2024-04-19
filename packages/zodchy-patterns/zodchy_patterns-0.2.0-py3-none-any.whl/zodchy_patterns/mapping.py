import collections.abc
import enum


class Reference:
    def __init__(self, data: collections.abc.Mapping[int, enum.Enum]):
        self._data = data

    def __getitem__(self, key: int) -> enum.Enum:
        return self._data.get(key)

    def __len__(self) -> int:
        return len(self._data)

    def get(self, key: int):
        return self._data.get(key)

    def __call__(self, value: enum.Enum):
        for k, v in self._data.items():
            if v == value:
                return k
