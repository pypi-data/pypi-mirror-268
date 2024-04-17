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

from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum
from openfinance.agents.promptflow.percept.prompt import OPINION_PROMPT
from openfinance.agents.promptflow.percept.output_parser import TaskOutputParser


class PercepFlow(BaseFlow):
    name = "PercepFlow"
    inputs: List[str] = ["content"]
    prompt: PromptTemplate = OPINION_PROMPT
    parser: BaseParser = TaskOutputParser()

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        **kwargs: Any        
    ) -> 'PercepFlow':
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
        inputs["types"] = ",".join(EntityGraph().get_types())
        resp = await self.llm.acall(self.prompt.prepare(inputs))
        resp = self.parser.parse(resp.content)
        return {self.output: resp}