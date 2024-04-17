import asyncio
import json
from typing import Dict
from openfinance.config import Config
from openfinance.agentflow.llm.manager import ModelManager 
from openfinance.agents.role.manager import RoleManager
from openfinance.searchhub.task.base import Task

class RoleTask(Task):
    name = "role"
    def __init__(
        self
    ):
        self.config = Config()
        self.role_manager = RoleManager(config=self.config)

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
        #print("enter async")
        role = kwargs.get("role", "")
        result = await self.role_manager.get_role(role).acall(text)
        return {"result": result['output']}

if __name__ == '__main__':
    task = RoleTask() 
    result = asyncio.run(task.aexecute("Get GDP growth rate", role="Elon Musk"))
    print(result)