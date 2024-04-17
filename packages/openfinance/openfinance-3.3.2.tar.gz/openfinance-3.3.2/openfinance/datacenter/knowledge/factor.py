import asyncio
from typing import Any, Dict, List, Optional, Callable
from openfinance.datacenter.knowledge.executor import Executor
from openfinance.datacenter.knowledge.wrapper import wrapper

class Factor:
    '''
        class for factor, used in graph
    '''    
    def __init__(
        self,
        name: str,
        description: str,
        paths: List[List[str]],
        parents: List['Factor'] = [],
        childrens: Dict[str, 'Factor'] = {}, # childrens for different roads
        executor: Executor = None,
    ):
        self.name = name
        self.description = description
        self.paths = paths
        self.parents = parents
        self.childrens = childrens
        self.executor = executor

    @classmethod
    def create(
        cls,
        name: str,
        description: str
    ) -> 'Factor':
        return cls(name=name, description=description)

    def __call__(
        self,
        *args: Any,        
        **kwargs: Any        
    ) -> Any:
        """
            Args:
                    rootNode: original rootNode for choosing path
            Return:
                    list of dict
        """
        # print(self.name)
        # print(kwargs)
        exes = kwargs.get("executor", []) # get existed function
        if self.executor.name in exes:
            return 
        exes.append(self.executor.name)
        kwargs["executor"] = exes
        # print(self.childrens)
        # print(self.parents)
        # print(kwargs)
        result = self.executor(*args, **kwargs)
        if result:           
            if len(self.childrens):
                result = [result]
                for path, child in self.childrens.items():
                    # print(path, child.name)
                    if "-".join(exes) in path and child.executor: # if no excutor, drop it
                        # print(path, child.name)
                        child_ret = child(*args, **kwargs)
                        if child_ret: # if empty response, drop it
                            result.append(child_ret)
                return wrapper(result)
        return wrapper(result)

    async def acall(
        self,
        *args: Any,        
        **kwargs: Any        
    ) -> Any:
        """
            Args:
                    rootNode: original rootNode for choosing path
            Return:
                    list of dict
        """
        # print(self.name)
        # print(kwargs)
        exes = kwargs.get("executor", []) # get existed function
        if self.executor.name in exes:
            return 
        exes.append(self.executor.name)
        kwargs["executor"] = factors 
        # print(self.name, funcs, kwargs)
        # print(kwargs)
        result = await self.executor.acall(*args, **kwargs)
        if result:           
            if len(self.childrens):
                result = [result]
                for path, child in self.childrens.items():
                    if "-".join(exes) in path and child.executor: # if no excutor, drop it
                        child_ret = await child.acall(*args, **kwargs)
                        if child_ret: # if empty response, drop it
                            result.append(child_ret)
                return wrapper(result)
        return wrapper(result)


    def add_path(
        self, 
        paths
    ):
        self.paths.append(paths)

    def register_func(
        self, 
        func: Executor
    ):
        self.executor = func
    
    def add_parents(
        self, 
        parent: 'Factor'
    ):
        if parent not in self.parents:
            self.parents.append(parent)

    def get_parents(
        self
    ) -> List['Factor']:
        return self.parents

    def add_childrens(
        self, 
        paths,
        child: 'Factor'
    ):
        name = "-".join(paths)
        if name not in self.childrens:
            self.childrens[name] = child

    def get_childrens(
        self
    ) -> Dict[str, 'Factor']:
        return self.childrens