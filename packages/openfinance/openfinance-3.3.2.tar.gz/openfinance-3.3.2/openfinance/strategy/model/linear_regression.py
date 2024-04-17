import json

from typing import (
    Any,
    List,
    Dict
)

from openfinance.strategy.model.base import Model
from openfinance.strategy.feature.company import *
from openfinance.strategy.feature.market import *
from openfinance.strategy.feature.base import FeatureManager

DEFAULT = -100000

class LR(Model):
    features_to_weights: Dict[str, float]

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_file(
        cls,
        filename
    ) -> "LR":
        with open(filename, "r") as infile:
            jsondata = json.load(infile)
            name = jsondata["name"]
            features_to_weights = jsondata["weights"]
            return cls(
                name=name,
                features_to_weights=features_to_weights
            )

    def policy(
        self,
        *args,
        **kwargs    
    ):
        """
            data: dict(feature -> {stock: val})
        """
        name = kwargs.get("name")
        name_to_features = kwargs.get("name_to_features")
        result = DEFAULT
        for k, v in name_to_features.items():
            if name in v:
                result += self.features_to_weights[k] * v[name]
        if result != DEFAULT:
            return result - DEFAULT
        else: 
            return 
