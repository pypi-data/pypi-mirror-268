# flake8: noqa
import asyncio
import inspect
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
    SUFFIX,
    ROLE_PROMPT
)

from openfinance.agents.promptflow.function.output_parser import FunctionOutParser

class FuncFlow(BaseFlow):
    name = "FuncFlow"
    inputs: List[str] = ["content"]
    prompt: PromptTemplate = ROLE_PROMPT
    channel: str = "channel"
    parser: BaseParser = FunctionOutParser()

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    def create_prompt(
        self,
        tools: List[Tool]
    ) -> PromptTemplate:
        #print(tools)
        tool_strings = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
        tool_names = ", ".join([tool.name for tool in tools])
        format_instructions = FORMAT_INSTRUCTIONS.format(tool_names=tool_names)
        template = "\n\n".join([PREFIX, tool_strings, format_instructions, SUFFIX])
        return PromptTemplate(prompt=template, variables=["content"])

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
        tools = kwargs.pop("tools", [])
        prompt = self.create_prompt(tools)

        resp = await self.llm.acall(prompt.prepare(inputs))
        action = self.parser.parse(resp.content)

        result = ""
        for tool in tools:
            if tool.name == action.name:
                #action_input = kwargs.get("param", action.action_input)
                if kwargs:
                    action_input = kwargs
                # print(tool, action_input)
                iscoroutine = False
                if hasattr(tool.func, "__call__"): # check if it's a executor class
                    if inspect.iscoroutinefunction(tool.func.executor.func):
                        iscoroutine = True
                if inspect.iscoroutinefunction(tool.func):
                    iscoroutine = True
                if iscoroutine:
                    if isinstance(action_input, List): # to improve later
                        result = []
                        for i in action_input:
                            if isinstance(i, dict):
                                tmp_ret = await tool.acall(**i)
                            else:
                                tmp_ret = await tool.acall(i)
                            if isinstance(tmp_ret, str):
                                result.append({
                                    "result": tmp_ret
                                })
                            else:
                                result.append(tmp_ret)
                        return {self.output: result}
                    if isinstance(action_input, dict):
                        result = await tool.acall(**action_input)
                    else:
                        result = await tool.acall(action_input)
                    break  
                else:
                    if isinstance(action_input, List):
                        result = []
                        for i in action_input:
                            if isinstance(i, dict):
                                tmp_ret = tool(**i)
                            else:
                                tmp_ret = tool(i)
                            if isinstance(tmp_ret, str):
                                result.append({
                                    "result": tmp_ret
                                })
                            else:
                                result.append(tmp_ret)
                        return {self.output: result}
                    if isinstance(action_input, dict):
                        result = tool(**action_input)
                    else:
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