import asyncio
import copy
from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)
from openfinance.agents.agent.agent_prompt import (
    ROLE_PROMPT,
    TOOL_PROMPT,
    POST_PROMPT,
    MEM_PROMPT
)
from openfinance.agentflow.llm.base import BaseLLM
from openfinance.agentflow.flow.agent_base import AgentBase

from openfinance.agentflow.base_parser import BaseParser
from openfinance.agents.agent.output_parser import SingleActionParser

class Agent(AgentBase):
    name: str = "agent"
    role: str
    goal: str
    parser: BaseParser = SingleActionParser()

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_scratch(
        cls,
        llm: BaseLLM,
        **kwargs: Any        
    ) -> "Agent":

        prompt = POST_PROMPT

        if "role" not in kwargs and "goal" not in kwargs:
            raise f"role and goal is necessary"

        prompt + ROLE_PROMPT.prepare({
            "role": kwargs.get("role"),
            "goal": kwargs.get("goal")
        })
        tools = kwargs.pop("tools", {})
        skills = kwargs.pop("skills", {})
        tools_desc = "\n".join([k + ": " + v.description for k, v in tools.items()])
        tool_names = ",".join(list(tools.keys()))
        prompt + "\n"
        prompt + TOOL_PROMPT.prepare({"tools":tools_desc, "tool_names":tool_names})
        #print(prompt)
        return cls(
            llm=llm,
            prompt=prompt,
            tools=tools,
            skills=skills,
            **kwargs
        )

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
        prompt = copy.deepcopy(self.prompt)
        if self.memory.history:
            prompt + "\n"
            prompt + MEM_PROMPT.prepare({"chat_history": self.memory()})
            kwargs["document"] = self.memory()
        resp = await self.llm.acall(prompt.prepare(inputs))
        action = self.parser.parse(resp.content)
        print("action", action)
        if action.name == "Final":
            return {self.output: action.action_input, "finish": True}
        if action.name in self.tools:
            tool = self.tools[action.name] 

        result = await tool.acall(action.action_input, **kwargs)
        self.memory.add("Action", action.action_input)
        self.memory.add("Observation", result["output"])
        return result