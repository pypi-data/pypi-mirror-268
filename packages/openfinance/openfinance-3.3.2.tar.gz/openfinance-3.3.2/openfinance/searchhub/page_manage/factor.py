import json
from typing import Any, Dict, List
from openfinance.searchhub.page_manage.base import BaseElement
from openfinance.datacenter.knowledge.graph import Graph
class Factor(BaseElement):
    stype: str = "Factor"

class FactorManager:
    type_to_ele: Dict[str, Factor] = {}
    graph: Graph = None

    def __init__(
        self, 
        graph
    ):
        self.graph = graph

    def register(
        self, 
        name: str, 
        base: Factor
    ) -> None:
        if name not in self.type_to_ele:
            self.type_to_ele[name] = base

    def get(
        self, 
        name: str
    ) -> Factor:
        return self.type_to_ele.get(name, None)

    # will be moved to db later
    def get_details(
        self, 
        factor: str
    ) -> Dict[str, Any]:
        return {
            "factor": factor,
            "icon": "",
            "jump_url": "",
        }

    def get_homepage(
        self, 
        num: int
    ) -> Dict[str, Any]:
        '''
            level 2 category
        '''
        result = {}
        for head in self.graph.headers:
            result[head] = []
            for ele in self.graph.get_factor(head).get_childrens():
                result[head].append(
                    self.get_details(
                        ele.name
                    )
                )
        return result