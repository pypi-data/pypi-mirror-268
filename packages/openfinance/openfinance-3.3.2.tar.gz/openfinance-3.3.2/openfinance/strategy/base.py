import asyncio
import aiohttp
import json

from abc import ABC, abstractmethod
from functools import reduce

from typing import (
    Any,
    List,
    Dict
)
from pydantic import BaseModel, root_validator

from openfinance.datacenter.knowledge.entity_graph import EntityGraph
from openfinance.strategy.model.base import Model

class Strategy(ABC, BaseModel):
    name: str
    desc: str
    name_to_features: Dict[str, Any]
    model: Model

    def run(
        self,
        *args,
        **kwargs    
    ):
        """
            data: dict(feature -> {stock: val})
        """
        if "candidates" not in kwargs:
            kwargs["candidates"] = list(EntityGraph().companies.keys())

        if "features" not in kwargs:
            kwargs["features"] = {k: v.run(*args, **kwargs) for k, v in self.name_to_features.items()}

        result = self.model.run(*args, **kwargs)

        return result

    def features(
        self,
        *args,
        **kwargs    
    ):
        """
            data: dict(feature -> {stock: val})
        """
        if "candidates" not in kwargs:
            kwargs["candidates"] = list(EntityGraph().companies.keys())

        if "features" not in kwargs:
            kwargs["features"] = {k: v.run(*args, **kwargs) for k, v in self.name_to_features.items()}

        return kwargs["features"]

    def fetch(
        self,
        *args,
        **kwargs
    ) -> List[Any]:
        """
            Function to fetch candidates with restrictions
            format: params: list[key, mode, condition]
            ex: a.fetch(params=[("OperationGrow", "gt", 10), ("OperationSpeedAcc", "lt", 10)])
        """
        if "params" not in kwargs:
            raise  f"pls input restrictions"
        params = kwargs["params"]
    
        values = []
        for i in params:
            values.append(self.name_to_features[i[0]].fetch(
                mode=i[1],
                thresh=i[2]
            ))
        keys = reduce(lambda a,b: a&b, map(dict.keys, values)) 
        return keys