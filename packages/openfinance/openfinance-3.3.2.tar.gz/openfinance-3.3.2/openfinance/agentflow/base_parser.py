from typing import (
    Any
)

from abc import ABC, abstractmethod

class BaseParser(ABC):
    name:str

    @abstractmethod
    def parse(
        self,
        text: str
    ) -> Any:
        """Base Parser"""
