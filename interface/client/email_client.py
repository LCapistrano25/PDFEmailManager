from abc import ABC, abstractmethod
from typing import Iterable

class EmailClient(ABC):
    """Responsável por realizar as operações com o email"""

    @abstractmethod
    def box(self, criteria) -> None:
        pass

    @abstractmethod
    def get_unread_emails(self) -> Iterable:
        pass

    @abstractmethod
    def mark_as_read(self, uid: str) -> None:
        pass

    @abstractmethod
    def move_to_folder(self, uid: str, folder: str) -> None:
        pass

    @abstractmethod
    def delete(self, uid: str) -> None:
        pass

    @abstractmethod
    def create_folder(self, folder: str) -> None:
        pass

    @abstractmethod
    def exist_folder(self, folder: str) -> bool:
        pass