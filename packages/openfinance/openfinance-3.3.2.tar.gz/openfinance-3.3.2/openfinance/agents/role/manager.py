import asyncio
from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)

from openfinance.config import Config
from openfinance.agentflow.llm.manager import ModelManager 

from openfinance.agents.role.prompts import roles_prompts
from openfinance.agents.role.role_base import RoleBase

class RoleManager:
    def __init__(
        self,
        config
    ):
        self.name_to_role = {}
        model_type = config.get("role_manager")
        if not model_type:
            model_type = "chatgpt"
        self.llm = ModelManager(config).get_model(model_type)
        for name, prompt in roles_prompts.items():
            self.create_role(name.lower(), prompt)

    def create_role(
        self,
        name, 
        prompt
    ):
        if name not in self.name_to_role:
            self.name_to_role[name] = RoleBase.from_llm(llm=self.llm, prompt=prompt)
    
    def get_role(
        self, 
        name: str
    ):
        name = name.lower()
        return self.name_to_role.get(name, self.llm)

    def extract_role(
        self,
        query: str
    ) -> Dict[str, str]:
        """
        Extract task name and fix query for input
        """
        for t in roles_prompts:
            if query.upper().startswith("@" + t):
                return {
                    "role": t,
                    "query": query[len(t)+1:]
                }
        return {"query": query}