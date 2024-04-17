import asyncio
from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)
from openfinance.agentflow.flow.base import BaseFlow
from openfinance.agentflow.llm.chatgpt import ChatGPT
from openfinance.agentflow.llm.base import BaseLLM
from openfinance.agentflow.base_parser import BaseParser
from openfinance.agentflow.prompt.base import PromptTemplate
from openfinance.searchhub.recall.base import IndexManager


from openfinance.agents.promptflow.summary.prompt import PROMPT

class SummaryFlow(BaseFlow):
    name = "SummaryFlow"
    description = "Summary Informations to answer questions"
    inputs: List[str] = ["content", "document"]
    prompt: PromptTemplate = PROMPT

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        **kwargs: Any        
    ) -> 'SummaryFlow':
        return cls(llm=llm, **kwargs)

    async def acall(
        self,
        content: str,
        **kwargs: Any        
    ) -> Dict[str, str]:

        inputs = {"content": content}
        for i in self.inputs:
            if i != "content":
                inputs[i] = kwargs[i]
        for k, v in inputs.items():
            if not isinstance(v, str):
                inputs[k] = str(v)
        resp = await self.llm.acall(self.prompt.prepare(inputs))
        return {self.output: resp.content}

if __name__ == "__main__":
    model = ChatGPT(
        model = "gpt-3.5-turbo",
        api_key = "",
        base_url = ""
    )
    flow = SummaryFlow.from_llm(model)
    result = asyncio.run(flow._acall(input="TSLA"))
    print(result)