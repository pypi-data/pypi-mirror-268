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
from openfinance.strategy.model.index_sort import IndexSort
from openfinance.strategy.feature.base import FeatureManager


class CompanyIndexSort(Strategy):
    name = "CompanyIndexSort"
    desc = "CompanyIndexSort"

    @classmethod
    def from_file(
        cls,
        filename="openfinance/strategy/models/LR/operation.json"
    ) -> "CompanyIndexSort":
        model = IndexSort.from_file(filename)
        name_to_features = {k: FeatureManager().get(k) for k in model.features_to_weights.keys()}
        return cls(
            model=model, 
            name_to_features=name_to_features
        )

if __name__== "__main__":
    policy = CompanyIndexSort.from_file()

    # Step 1: choose candidates stocks
    candidates = policy.fetch(
        params=[
            # ("OperationGrow", "gt", 10), 
            # ("DividentMean", "gt", 3),
            # ("DividentSpeed", "gt", 0.1),            
            # ("OperationSpeedAcc", "lt", 10),
            # ("ProfitGrow", "gt", 10),
            # ("ProfitSpeedAcc", "lt", 10),
            # ("GrossProfit", "gt", 100),
            ("PriceEarning", "lt", 80),
            ("PriceEarning", "gt", 10) 
            # ("MoneyFlowDirect", "gt", 0)
        ])  
    print(candidates)

    # Step 2: evaluate candidates stocks
    # A Bug for invisible values
    result = policy.run(
        #candidates = ["万润新能", "石英股份", "恒誉环保", "贵州茅台", "山外山", "冠农股份", "分众传媒","嘉益股份", "海澜之家"],
        candidates = list(candidates),
        reverse = {
            "OperationGrow": True,
            "ProfitGrow": True,
            "GrossProfit": True,
            "ProfitSpeedAcc": True,
            "OperationSpeedAcc": True,
            "NetProfitRatio": True,
            "ROE": True,
            "DividentSpeed": True,
            "DividentMean": True,
            "GrossProfitYoY": True,
            "FreeCashFlowYield": True,
            "NetCashFlowYoY": True,
            "FreeCashRatio": True,
            "WinCostDist": True,
            "MoneyFlowDirect": True
        },
        negative = {
            "PriceEarning": True
        },
        from_db=True,
        type="company"
    )

    # # Step 3: sort results
    result = sorted(result.items(), key=lambda x: x[1])
    print(result)
    stocks = [v[0] for v in result]
    features = policy.features(
        candidates=stocks,
        from_db=True,
        type="company"
    )
    print(json.dumps(features, indent=4, ensure_ascii=False))