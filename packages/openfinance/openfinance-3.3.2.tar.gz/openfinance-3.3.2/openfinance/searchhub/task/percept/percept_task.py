import asyncio
import json
from typing import Dict
from openfinance.config import Config
from openfinance.agentflow.llm.manager import ModelManager 
from openfinance.searchhub.recall.base import IndexManager
from openfinance.searchhub.recall.channel import analysis

from openfinance.datacenter.knowledge.graph import Graph
from openfinance.utils.recall.faiss import Faiss
from openfinance.utils.recall.es import ES
from openfinance.datacenter.knowledge.executor import ExecutorManager
from openfinance.utils.embeddings.embedding_manager import EmbeddingManager
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

from openfinance.agents.promptflow.percept.opinion import PercepFlow
from openfinance.agents.promptflow.percept.match import MatchFlow

from openfinance.searchhub.task.base import Task

class PerceptTask(Task):
    name = "percept"
    def __init__(
        self
    ):
        self.config = Config()
        self.llm = ModelManager(self.config).get_model("aliyungpt")

        index_manager = self._init_index()

        self.percept = PercepFlow.from_llm(
            self.llm, 
        )
        self.match = MatchFlow.from_llm(
            self.llm,
            index_manager
        )

    def  _init_index(
        self
    ) -> IndexManager:
        index_manager = IndexManager()
        save_local = True
        if not save_local:
            graph = Graph.build_from_file(
                "openfinance/datacenter/knowledge/schema.md"
            )
            graph.assemble(ExecutorManager())
            db = Faiss.from_embedding(
                inputs = graph.factors, 
                embedding = EmbeddingManager.get_embedding(
                    self.config.get("index")[self.name]
                )
            )
            db.save("openfinance/datacenter/local_data", "factor")
            industry_db = Faiss.from_embedding(
                inputs = list(EntityGraph().industries),
                embedding = EmbeddingManager.get_embedding(
                    self.config.get("index")[self.name]
                )
            )
            industry_db.save("openfinance/datacenter/local_data", "industry")            
            company_db = Faiss.from_embedding(
                inputs = list(EntityGraph().companies.keys()),
                embedding = EmbeddingManager.get_embedding(
                    self.config.get("index")[self.name]
                )
            )
            company_db.save("openfinance/datacenter/local_data", "company")            
        else:
            db = Faiss.load(
                embedding = EmbeddingManager.get_embedding(
                    self.config.get("index")[self.name]),
                folder_path = "openfinance/datacenter/local_data", 
                index_name = "factor"                
            )
            industry_db = Faiss.load(
                embedding = EmbeddingManager.get_embedding(
                    self.config.get("index")[self.name]),
                folder_path = "openfinance/datacenter/local_data", 
                index_name = "industry"                
            )
            company_db = Faiss.load(
                embedding = EmbeddingManager.get_embedding(
                    self.config.get("index")[self.name]
                ),
                folder_path = "openfinance/datacenter/local_data", 
                index_name = "company"                
            )
        index_manager.register(self.name, db)
        index_manager.register(EntityEnum.Industry.type, industry_db)
        index_manager.register(EntityEnum.Company.type, company_db)
        return index_manager

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
        percept_data = await self.percept.acall(**{
            "content": text
        })

        result = await self.match.acall(**{
            "content": percept_data["output"],
            "channel": self.name,         
        })
        
        return {"result": result['output']}


if __name__ == '__main__':
    task = PerceptTask() 
    try:
        import time
        from openfinance.robot.wechatpro.base import WechatPro
        from openfinance.datacenter.database.source.event.caixing import get_caijing_news, caixing_parse
        q = list()
        robot = WechatPro(Config().get("robot"))
        max_len = 10
        # for test
        while True:
            docs = get_caijing_news()
            for d in json.loads(docs)[:3]:
                url = d["url"]
                sid = d["contentid"]
                if sid not in q:
                    q.append(sid)
                else:
                    continue
                if len(q) == max_len:
                    q.pop(0)
                content = caixing_parse(url)
                print(content)
                result = asyncio.run(task.aexecute(content))
                print("result", result)
                # if len(result["result"].get("consequence", "")):
                #     result["result"]["url"] = url
                #     robot.push(**{
                #         "msgtype": "text",
                #         "text": result["result"]
                #     })
                # time.sleep(2)
            time.sleep(120)
    except Exception as e:
        print (e)    
        #result = asyncio.run(task.aexecute("比亚迪利润大幅提升"))
        #print(result)