import random
import json
from typing import Any, Dict, List
from openfinance.searchhub.page_manage.base import BaseElement
from openfinance.datacenter.knowledge.graph import Graph
from openfinance.datacenter.knowledge.executor import Executor

class Model(BaseElement):
    stype: str = "Model"

class ModelManager:
    type_to_ele: Dict[str, Model] = {}
    graph: Graph = None

    def __init__(
        self,
        graph
    ):
        self.graph = graph

    def register(
        self, 
        name: str, 
        base: Model
    ) -> None:
        if name not in self.type_to_ele:
            self.type_to_ele[name] = base

    def get(
        self, 
        name: str
    ) -> Model:
        return self.type_to_ele.get(name, None)

    # will be moved to db later
    def get_details(
        self, 
        data: Dict[str, Any]
    ) -> Dict[str, Any]:
        #print(data)
        return {
            "model": data["model"],
            "icon": "",
            "author": data["signature"],
            "tag": data['tag'],
            "time": "Updated " + str(random.randint(1,30)) + " days ago",
            "download": str(random.randint(1,1000)),
            "like": str(random.randint(1,200)),
            "jump_url": "",
        }

    def get_homepage(
        self, 
        num: int
    ) -> Dict[str, Any]:
        result = []
        for (name, exe) in self.graph.get_all_exec():
            result.append(self.get_details({
                "model": name,
                "tag": exe.description,
                "signature": exe.signature
            }))
        return result


    def get_factor_model(
        self, 
        factor: str, 
        num: int
    ) -> Dict[str, Any]:
        result = []
        for (name, exe) in self.graph.get_factor_exec(factor):
            result.append(self.get_details({
                "model": name,
                "tag": exe.description,
                "signature": exe.signature
            }))
        return result


#print(ModelManager().get_homepage(20))

#data = ModelManager().get_factor_model("Company Analysis", 20)
