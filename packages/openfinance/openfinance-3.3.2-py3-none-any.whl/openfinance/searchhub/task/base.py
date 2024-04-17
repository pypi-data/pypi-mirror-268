from typing import Dict
from abc import ABC, abstractmethod
import asyncio

class Task(ABC):
    name = "task"
    output = "result"
    
    @abstractmethod
    def execute(
        self, 
        text, 
        **kwargs
    ) -> Dict[str, str]:
        pass

    async def aexecute(
        self, 
        text, 
        **kwargs
    ) -> Dict[str, str]:
        return self.execute(
            text,
            kwargs
        )        