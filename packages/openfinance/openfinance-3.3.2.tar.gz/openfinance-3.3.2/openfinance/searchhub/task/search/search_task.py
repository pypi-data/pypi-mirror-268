import asyncio
import json
from typing import Dict
from openfinance.config import Config

from openfinance.searchhub.task.base import Task
from openfinance.agentflow.llm.manager import ModelManager 

from openfinance.agents.agent.base import Agent
from openfinance.agents.tool.search import SearchTool
from openfinance.service.base import wrapper_return

class SearchTask(Task):
    name = "search"
    def __init__(
        self
    ):
        self.agent = Agent.from_scratch(
            llm = ModelManager(Config()).get_model("aliyungpt"),
            role="Stock Analyst",
            goal="Provide professional and helpful advices",
            tools={"search": SearchTool.create()}
        )

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
        result = await self.agent.tools["search"].acall(
            text, **kwargs
        )
        websocket = kwargs.get("websocket", None)

        cache = ""
        if isinstance(result["output"], list):          
            for it in result["output"]:
                if websocket:
                    if websocket.open:
                        await websocket.send(wrapper_return(
                            output = it
                        ))
                        cache += it["result"] + "\n"
                    else:
                        raise f"websocket lost"         
        else:
            if websocket:
                if websocket.open:
                    await websocket.send(wrapper_return(
                        output = result["output"]
                    ))
                else:
                    raise f"websocket lost"
        if websocket:
            if websocket.open:
                return {
                    "result": "为您找到以上信息",
                    "cache": cache
                    }
            else:
                raise f"websocket lost"
        else:
            return {"result": result["output"]}

if __name__ == '__main__':
    task = SearchTask() 
    result = asyncio.run(task.aexecute("Get Company Analysis", name="杰普特"))
    # print(result)
    # result = asyncio.run(task.agent.acall("国家债务规模"))
    print(result)