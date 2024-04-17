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

from openfinance.agents.promptflow.plan.prompt import PLAN_PROMPT
from openfinance.agents.promptflow.plan.output_parser import TaskOutputParser

class PlanFlow(BaseFlow):
    name = "PlanFlow"
    description = "Divide a complicated task to subtasks"
    inputs: List[str] = ["content"]
    prompt: PromptTemplate = PLAN_PROMPT
    parser: BaseParser = TaskOutputParser()

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        **kwargs: Any        
    ) -> 'PlanFlow':
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
        resp = await self.llm.acall(self.prompt.prepare(inputs))
        print(resp)
        resp = self.parser.parse(resp.content)
        return {self.output: resp}

if __name__ == "__main__":
    model = ChatGPT(
        model = "gpt-3.5-turbo",
        api_key = "",
        base_url = ""
    )
    flow = PlanFlow.from_llm(model)
    result = asyncio.run(flow._acall(input="TSLA"))
    print(result)