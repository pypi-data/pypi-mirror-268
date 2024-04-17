import asyncio
import aiohttp
import json

from abc import ABC, abstractmethod

from typing import (
    Any,
    List,
    Dict
)
from openfinance.strategy.model.linear_regression import LR
from openfinance.strategy.policy.base import Strategy
from openfinance.strategy.feature.base import FeatureManager

class MarketSentiment(Strategy):
    name = "MarketSentiment"
    desc = "MarketSentiment"
    @classmethod
    def from_file(
        cls,
        filename="openfinance/strategy/models/LR/market_sentiment.json"
    ) -> "IndexSortPolicy":
        model = LR.from_file(filename)
        name_to_features = {k: FeatureManager().get(k) for k in model.features_to_weights.keys()}
        return cls(
            model=model, 
            name_to_features=name_to_features
        )

if __name__== "__main__":
    policy = MarketSentiment.from_file(
        "openfinance/strategy/models/LR/market_sentiment.json"
    )
    result = policy.run(
        candidates = ["上证指数"],
        reverse = {
            "OperationGrow": True,
            "ProfitGrow": True,
            "GrossProfit": True
        },
        negative = {
            "PriceEarning": True
        },
        from_db=True,
        type="market",
        latest=True        
    )
    print(result)

    features = policy.features(
        candidates=["上证指数"],
        from_db=True,        
        type="market"
    )
    print(json.dumps(features, indent=4, ensure_ascii=False))