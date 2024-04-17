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

from openfinance.agentflow.flow.base import BaseFlow
from openfinance.agentflow.llm.base import BaseLLM
from openfinance.agentflow.memory.base import Memory
from openfinance.agentflow.tool.base import Tool
from openfinance.agentflow.base_parser import BaseParser
from openfinance.agentflow.prompt.base import PromptTemplate

class AgentBase(BaseFlow):
    name: str = "agentbase"
    inputs: List[str] = ["content"]

    tools: Dict[str, Tool]
    skills: Dict[str, Any]
    memory: Memory = Memory()
    prompt: PromptTemplate

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        prompt: PromptTemplate,
        **kwargs: Any        
    ) -> 'AgentBase':
        tools = kwargs.pop("tools", {})
        skills = kwargs.pop("skills", {})
        return cls(
            llm=llm, 
            prompt=prompt,
            tools=tools,
            skills=skills,
            **kwargs
        )

    def add_tool(
        self,
        name: str,
        tool: Any
    ):
        if name not in self.tools:
            self.tools[name] = tool

    def add_skill(
        self,
        name: str,
        skill: Any
    ):
        if name not in self.skills:
            self.skills[name] = skill

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