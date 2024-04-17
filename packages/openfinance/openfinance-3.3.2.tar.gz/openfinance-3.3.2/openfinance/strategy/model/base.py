import asyncio
import aiohttp
import json

from abc import ABC, abstractmethod

from typing import (
    Any,
    List,
    Dict
)
from pydantic import BaseModel, root_validator

class Model(ABC, BaseModel):
    """
        Build model to evaluate stocks
    """
    name: str
    def run(
        self,
        *args,
        **kwargs    
    ):
        """
            data: dict(feature -> {stock: val})
        """
        if "candidates" in kwargs:
            stocks = kwargs["candidates"]
            if isinstance(stocks, str):
                stocks = [stocks]

        if "features" in kwargs:
            name_to_features = kwargs["features"]

        result = {}
        for i in stocks:
            # print(i)
            ret = self.policy(name=i, name_to_features=name_to_features)
            if ret and ret != None:
                result[i] = ret

        return result

    @abstractmethod
    def policy(
        self,
        *args,
        **kwargs    
    ):
        """
            data: dict(feature -> {stock: val})
        """
        pass    