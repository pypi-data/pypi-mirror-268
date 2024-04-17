import asyncio
from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pydantic import BaseModel, root_validator

@dataclass
class Message:
    role: str = ""
    content: Union[str, Dict[str, Any]] = ""

    def format(
        self
    ):
        return [{
            "role": self.role,
            "content": self.content
        }]

class BaseLLM(ABC, BaseModel):
    name: str = "BaseLLM"
    version: str  = ""
    model: str
    client: Any = None
    temperature: float = 0.1
    top_p: float = 0.5
    top_k: float = 0.8
    max_tokens: int = 2048

    def __call__(
        self,
        content: Union[str, List[Dict[str, str]]],        
        **kwargs: Any
    ) -> Message:
        return self.call(content, **kwargs)
    
    # @abstractmethod
    def call(
        self, 
        content: Union[str, List[Dict[str, str]]],       
        **kwargs: Any
    ) -> Dict[str, str]:
        """base interface for call"""

    async def _acall(
        self,
        content: Union[str, List[Dict[str, str]]],       
        **kwargs: Any
    ) -> Message:
        return await self.acall(content, **kwargs)
    
    @abstractmethod
    async def acall(
        self, 
        content: Union[str, List[Dict[str, str]]],
        **kwargs: Any
    ) -> Dict[str, str]:
        """base interface for async call"""    