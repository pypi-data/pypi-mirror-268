import json
import copy
from typing import Any, Dict, List, Optional, Callable, Union
from openfinance.datacenter.knowledge.factor import Factor
from openfinance.datacenter.knowledge.executor import Executor, ExecutorManager

class Graph:
    name = "Temporal Financial Graph"
    factors: Dict[str, Factor] = {}
    headers: List[str] = []

    def __init__(
        self, 
        factors, 
        headers
    ):
        self.factors = factors
        self.headers = headers

    @classmethod
    def build_from_file(
        cls, 
        filename="openfinance/datacenter/knowledge/schema.md"
        #infofile="openfinance/datacenter/knowledge/schema.json",
    ) -> 'Graph':
        '''
            Use Stack to build graph
        '''
        stack = []
        factors = {}
        headers = []
        level = -1
        #name_to_info = json.load(open(infofile, "r"))
        with open(filename, "r") as infile:
            for l in infile:
                data = l.rstrip("").strip("\n").split("-")
                if len(data) == 1:
                    continue
                new_level = int(len(data[0])/3) # length of shifttab
                name = data[1].strip()

                if 0 == new_level:
                    headers.append(name)    
                if new_level > level:
                    stack.append(name)
                elif new_level == level:
                    stack[-1] = name
                else:
                    stack = stack[:new_level]
                    stack.append(name)
                # print(l, new_level, level, name, stack)
                if name not in factors:
                    factors.update(
                        {
                            name: Factor(
                                name, 
                                "",
                                [copy.deepcopy(stack)],
                                [],
                                {},
                                None
                            )
                        }  # a deep hole here for python object memory allocation
                    )
                else:
                    factors[name].add_path(copy.deepcopy(stack))

                level = new_level
                if level > 0:
                    factors[name].add_parents(
                        factors[stack[-2]]
                    )
                    factors[stack[-2]].add_childrens(
                        stack, factors[name]
                    )
        # print(factors)
        return cls(factors, headers)

    def show(
        self
    ):
        for n, f in self.factors.items():
            print("*"*10, f.name, "*"*10)
            for p in f.get_parents():
                print("parents:", p.name)
            for c in f.get_childrens():
                print("children:", c.name)
    
    def get_factor(
        self, 
        name
    ) -> Factor:
        if name in self.factors:
            return self.factors[name]
        raise f"No Element called {name}"

    #  downgrade, will drop in future
    def assemble_func(
        self, 
        name, 
        func
    ):
        self.factors[name].register_func(
            Executor.from_func(func, self.factors[name].description)
        )

    #  downgrade, will drop in future
    def assemble(
        self, 
        funcs: Union[List[Dict[str, Callable]], Dict[str, Callable]]
    ):
        if isinstance(funcs, List):
            for term in funcs:
                for name, func in term.items():
                    self.assemble_func(name, func)
        else:
            for name, func in funcs.items():
                self.assemble_func(name, func)

    def assemble(
        self, 
        manager: ExecutorManager,
        user: str = "default"     
    ):
        for name_signature, exe in manager.name_to_executor.items():
            d = name_signature.split("|")
            name = d[0]
            signature = d[1]
            if not exe.graph_node:
                continue
            # print(name, signature, user)
            if signature == user and name in self.factors:
                self.factors[name].description = exe.description
                self.factors[name].register_func(
                    exe
                )

    def get_available_executors(
        self,
        filters: List[str] = []
    ):
        '''
            Based on user's requirements, return funcs
            :factor_to_models, user require
        '''
        desc_to_func = {}
        for name, factor in self.factors.items():
            if name in filters:
                continue
            if factor.executor:
                desc_to_func.update({factor.name : factor.executor})  # recall by name
                desc_to_func.update({factor.description : factor.executor})  # recall by description
        return desc_to_func

    def get_all_exec(
        self
    ):
        '''
            Based on user's requirements, return execs
        '''
        desc_to_func = []
        for name, factor in self.factors.items():
            if factor.executor:
                desc_to_func.append((name, factor.executor))
        return desc_to_func

    def get_factor_exec(
        self,
        factor: str
    ):
        '''
            return factor and children func
        '''
        desc_to_func = []
        factor = self.factors[factor]
        def inner_func(factor, desc_to_func):
            if factor.executor:
                desc_to_func.append((factor.name, factor.executor))
            for chd in factor.get_childrens():
                desc_to_func = inner_func(chd, desc_to_func)
            return desc_to_func
        return inner_func(factor, desc_to_func)

if __name__ == "__main__":
    graph = Graph.build_from_file("openfinance/datacenter/knowledge/schema.md")
    graph.show()