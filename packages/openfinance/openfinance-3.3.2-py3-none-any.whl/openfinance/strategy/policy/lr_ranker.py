import asyncio
import aiohttp
import json

from abc import ABC, abstractmethod

from typing import (
    Any,
    List,
    Dict
)

from openfinance.strategy.policy.base import Strategy
from openfinance.strategy.model.linear_regression import LR
from openfinance.strategy.feature.base import FeatureManager


class OperationPolicy(Strategy):
    name = "OperationPolicy"
    desc = "OperationPolicy"

    @classmethod
    def from_file(
        cls,
        filename="openfinance/strategy/models/LR/operation.json"
    ) -> "OperationPolicy":
        model = LR.from_file(filename)
        name_to_features = {k: FeatureManager().get(k) for k in model.features_to_weights.keys()}
        return cls(
            model=model, 
            name_to_features=name_to_features
        )

if __name__== "__main__":
    pl = OperationPolicy.from_file()
    print(pl.fetch(params=[
        ("OperationGrow", "gt", 10), 
        #("DividentSpeed", "gt", 0.01),
        #("OperationSpeedAcc", "lt", 10),
        ("ProfitGrow", "gt", 10),
        #("ProfitSpeedAcc", "lt", 10),
        ("GrossProfit", "gt", 100)        
        ]))
    result = pl.run(
        from_db=True,
        type="company"        
    )