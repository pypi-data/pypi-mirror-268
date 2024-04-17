import asyncio
import json
from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)

from openfinance.config import Config
from openfinance.agentflow.llm.manager import ModelManager 
from openfinance.searchhub.recall.base import IndexManager
from openfinance.searchhub.recall.channel import search
from openfinance.datacenter.knowledge.graph import Graph

from openfinance.utils.recall.faiss import Faiss
from openfinance.utils.recall.es import ES

from openfinance.datacenter.knowledge.executor import ExecutorManager
from openfinance.utils.embeddings.embedding_manager import EmbeddingManager

from openfinance.agents.promptflow.factor.base import RecallFlow
from openfinance.agents.promptflow.function.base import FuncFlow
from openfinance.agentflow.tool.base import Tool


class SearchTool(Tool):
    description = "Get result for explicit indicator or easy query"
    func: Callable = None
    recall: RecallFlow
    func: FuncFlow

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def create(cls) -> "SearchTool":
        name = "search"
        config = Config()
        llm = ModelManager(config).get_model("aliyungpt")
        graph = Graph.build_from_file(
            "openfinance/datacenter/knowledge/schema.md"
        )
        graph.assemble(ExecutorManager())
        index_manager = IndexManager()
        db = Faiss.from_embedding(
            inputs = ExecutorManager().build_recall(),
            embedding = EmbeddingManager.get_embedding(
                config.get("index")[name]
            )
        )
        index_manager.register(name, db)
        recall = RecallFlow.from_llm(
            llm, 
            index_manager,
            graph
        )
        func = FuncFlow.from_llm(
            llm
        )
        return cls(name=name, recall=recall, func=func)

    async def acall(
        self, 
        text, 
        **kwargs
    ) -> Dict[str, str]:
        #print("enter async")     
        recall_data = await self.recall.acall(**{
            "content": text, 
            "channel": self.name
            })
        print("tools", recall_data)

        kwargs["tools"] = recall_data["output"]
        result = await self.func.acall(
            text,
            **kwargs
        )
        return result

if __name__ == "__main__":
    tool = SearchTool.create()
    result = asyncio.run(tool.acall("地方债务规模"))
    print(result)