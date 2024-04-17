# flake8: noqa
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
from openfinance.agentflow.tool.base import Tool

from openfinance.agents.promptflow.function.prompt import (
    PREFIX,
    FORMAT_INSTRUCTIONS,
    SUFFIX
)

from openfinance.agents.promptflow.function.output_parser import FunctionOutParser

class FuncFlow(BaseFlow):
    name = "FuncFlow"
    inputs: List[str] = ["content"]
    channel: str = "channel"
    parser: BaseParser = FunctionOutParser()

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    def create_prompt(
        self,
        name_to_tools: Dict[str, List[Tool]]
    ) -> str:
        #print(tools)
        prompt = """Choose tools for the following questions. """
        for name, tool in name_to_tools.items():
            prompt += "Quesiton: " + k
            prompt += ", you can choose one of [" + ", ".join([tool.name for tool in tools]) + "]"
            prompt += "\n" + "\n".join([f"{tool.name}: {tool.description}" for tool in tools])

        template = "\n\n".join([PREFIX, FORMAT_INSTRUCTIONS, SUFFIX])
        return template

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        **kwargs: Any        
    ) -> 'FuncFlow':
        #prompt = cls.create_prompt(tools)
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
        tools = kwargs.get("tools", [])
        prompt = self.create_prompt(tools)

        resp = await self.llm.acall(prompt)
        action = self.parser.parse(resp.content)

        result = ""
        for tool in tools:
            if tool.name == action.name:
                action_input = kwargs.get("param", action.action_input)
                print(tool, action_input)
                if isinstance(action_input, List):
                    result = []
                    for i in action_input:
                        tmp_ret = tool(i)
                        if isinstance(tmp_ret, str):
                            result.append({
                                "result": tmp_ret
                            })
                        else:
                            result.append(tool(i))
                    return {self.output, result}
                result = tool(action_input)
                break
        if isinstance(result, str):
            return {self.output: {"result": result}}
        else:
            return {self.output: result}

if __name__ == "__main__":
    model = ChatGPT(
        model = "gpt-3.5-turbo",
        api_key = "",
        base_url = ""
    )
    flow = FuncFlow.from_llm(model, [])
    result = asyncio.run(flow._acall(input="TSLA"))
    print(result)