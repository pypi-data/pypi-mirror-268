# flake8: noqa
import asyncio
from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)
from openfinance.searchhub.recall.base import IndexManager

from openfinance.agentflow.flow.base import BaseFlow
from openfinance.agentflow.llm.chatgpt import ChatGPT
from openfinance.agentflow.llm.base import BaseLLM
from openfinance.agentflow.tool.base import Tool

class RecallFlow(BaseFlow):
    name = "RecallFlow"
    inputs: List[str] = ["content"]
    channel: str = "channel"
    index_manager: IndexManager

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        index_manager : IndexManager,         
        **kwargs: Any        
    ) -> 'RecallFlow':
        return cls(llm=llm, index_manager=index_manager, **kwargs)

    async def acall(
        self,
        content: str,
        **kwargs: Any        
    ) -> Dict[str, str]:
        docs = self.index_manager.search(
            kwargs[self.channel],
            content
            )
        tools = []
        tool_names = []
        for exe in docs:
            print("The functions is :", exe.func)
            if exe.func in tool_names:
                continue
            tool_names.append(exe.func)
            tools.append(Tool(
                name = exe.func.__name__,
                func = exe.func,
                description = exe.description
            ))
            # to add args to each function
        return {self.output: tools}

if __name__ == "__main__":
    model = ChatGPT(
        model = "gpt-3.5-turbo",
        api_key = "",
        base_url = ""
    )
    index_manager = IndexManager()
    flow = RecallFlow.from_llm(model, index_manager)
    result = asyncio.run(flow._acall(input="TSLA"))
    print(result)