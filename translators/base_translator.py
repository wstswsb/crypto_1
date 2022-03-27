from abc import ABC, abstractmethod


class BaseTranslator(ABC):
    @abstractmethod
    def to_dict(self, model) -> dict[str, int]:
        pass

    @abstractmethod
    def from_db_tuple(self, db_tuple: tuple[int]):
        pass
