import asyncio
import json
from typing import Dict
from openfinance.config import Config

from openfinance.agents.agent.base import Agent
from openfinance.agentflow.llm.manager import ModelManager 
from openfinance.agents.tool.factor_search import FactorSearchTool

from openfinance.agents.promptflow.plan.base import PlanFlow
from openfinance.agents.promptflow.data_analysis.base import DataAnalysisFlow
from openfinance.agents.promptflow.summary.base import SummaryFlow

from openfinance.searchhub.recall.channel import analysis
from openfinance.datacenter.knowledge.graph import Graph
from openfinance.datacenter.knowledge.executor import ExecutorManager

from openfinance.datacenter.echarts.base import ChartManager
from openfinance.service.base import wrapper_return
from openfinance.searchhub.task.base import Task

class FixedAnalysisTask(Task):
    name = "fanalysis"

    def __init__(
        self
    ):
        llm = ModelManager(Config()).get_model("aliyungpt")
        self.agent = Agent.from_scratch(
            llm = llm,
            role="Stock Analyst",
            goal="Try your best to provide professional and helpful financial advices",
            tools={
                "search": FactorSearchTool.create()
            },
            skills={
                "plan":  PlanFlow.from_llm(llm),
                "summary": SummaryFlow.from_llm(llm),
                "data_analysis": DataAnalysisFlow.from_llm(llm)
            }
        )

        self.graph = Graph.build_from_file(
            "openfinance/datacenter/knowledge/schema.md"
        )
        self.graph.assemble(ExecutorManager())

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
        # print("enter async")
        # plan_data = await self.agent.skills["plan"].acall(**{
        #     "content": text
        # })
        plan_data = {}
        plan_data["output"] = {
            "Fundamental Analysis": [],
            "Technical Analysis": [],
            "Sentiment Analysis": [],
            "Industry Analysis": [],
            "Market Analysis": [],
            "Macro Economic": []
        }

        websocket = kwargs.get("websocket", None)

        chart = ChartManager().get("tree")(plan_data['output'])
        if websocket:
            if websocket.open:
                await websocket.send(wrapper_return(
                    output=f"\n{text}正在从基于以下维度分析，请耐心等待...\n", chart=chart
                ))
            else:
                raise f"websocket lost"
        
        #summary_data = {}
        summary_data = ""
        for item in plan_data["output"].keys():
            # result = await self.agent.tools["search"].acall(
            #     item,
            #     **kwargs
            # )
            result = {"output": self.graph.get_factor(item)(kwargs.get("company"))}
            print(result)
            if isinstance(result["output"], list):
                #summary_data += "Step(" + item + "):---\n"
                summary_data += "Factor(" + item + "):\n---\n"
                analysis_data = ""
                for it in result["output"]:
                    if it["result"]:
                        # summary_data += it["result"] + "\n"
                        analysis_data += it["result"] + "\n"
                        # if websocket:
                        #     if websocket.open:
                        #         await websocket.send(wrapper_return(
                        #             output = it
                        #         ))
                        #     else:
                        #         raise f"websocket lost"
                analysis_result = await self.agent.skills["data_analysis"].acall(
                    **{"content": analysis_data}
                )
                if websocket:
                    if websocket.open:
                        await websocket.send(wrapper_return(
                            output = item
                        ))                        
                        await websocket.send(wrapper_return(
                            output = analysis_result["output"]
                        ))
                    else:
                        raise f"websocket lost"
                summary_data += analysis_result["output"] + "\n"
                summary_data += "---\n"
            else:
                if websocket:
                    if websocket.open:
                        await websocket.send(wrapper_return(
                            output = item
                        ))
                        await websocket.send(wrapper_return(
                            output = result["output"]
                        ))
                    else:
                        raise f"websocket lost"
                print(result)
                #summary_data[item] = result["output"]["result"]
                if result["output"]:
                    summary_data += "Task(" + item + "):\n" + result["output"]["result"] + "\n"
        
        result = await self.agent.skills["summary"].acall(**{
            "content": text,
            "document": str(summary_data)
        })
        print(result)
        return {"result": result['output']}

if __name__ == '__main__':
    task = FixedAnalysisTask()
    result = asyncio.run(task.aexecute("是否可以买入中视传媒的股票", company="中视传媒"))
    #result = asyncio.run(task.aexecute("为什么最近一直在下跌", company="华工科技"))
    #result = asyncio.run(task.aexecute("为什么游戏公司股价下跌这么多", company="游戏"))
    print(result)
