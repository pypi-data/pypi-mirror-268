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

from openfinance.agentflow.llm.base import BaseLLM

class BaseFlow(ABC, BaseModel):
    name: str
    llm: BaseLLM
    inputs: List[str]
    output: str = "output"
    
    def __call__(
        self,
        **kwargs: Any        
    ) -> Dict[str, str]:
        return self.call(**kwargs)

    def call(
        self,
        **kwargs: Any        
    ) -> Dict[str, str]:
        pass

    async def _acall(
        self,
        **kwargs: Any        
    ) -> Dict[str, str]:
        return await self.acall(**kwargs)

    @abstractmethod
    async def acall(
        self,
        **kwargs: Any        
    ) -> Dict[str, str]:
        """async func for flowCall"""