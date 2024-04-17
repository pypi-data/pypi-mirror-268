import asyncio
from typing import Dict

from openfinance.config import Config
from openfinance.agentflow.llm.manager import ModelManager
from openfinance.agents.promptflow.search_sql.text_to_sql.base import SearchSqlFlow
from openfinance.agents.promptflow.search_sql.recall_table.base import SearchSqlRecallFlow
from openfinance.searchhub.task.base import Task


class SearchSqlTask(Task):
    name = "search_sql"

    def __init__(self):
        self.config = Config()
        self.model_manager = ModelManager(config=self.config)
        self.llm = self.model_manager.get_model("chatgpt")
        self.search_sql_recall_flow = SearchSqlRecallFlow.from_llm(self.llm)
        self.search_sql_flow = SearchSqlFlow.from_llm(self.llm)

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
        tables = await self.search_sql_recall_flow.acall(**{
            "query": text
        })
        print(tables["output"])
        if len(tables["output"]) == 0:
            return {
                "result": "数据库中没有可以提供的信息。"
            }
        result = await self.search_sql_flow.acall(**{
            "query": text, "table": tables["output"]
        })
        if isinstance(result["output"], dict):
            return result["output"]
        return {"result" : result["output"]}

if __name__ == '__main__':
    task = SearchSqlTask()
    # result = asyncio.run(task.aexecute("过去半年国内cpi高于平均水平的时间里pmi数据如何"))
    # result = asyncio.run(task.aexecute("王子様喜欢谁"))
    # result = asyncio.run(task.aexecute("最近一年哪个公司股息较多"))
    result = asyncio.run(task.aexecute("*ST 正邦的销售地域分布"))
    print(result)
