import json
from functools import cmp_to_key

from typing import (
    Any,
    List,
    Dict
)

from openfinance.strategy.model.base import Model
from openfinance.strategy.feature.company import *
from openfinance.strategy.feature.market import *
from openfinance.strategy.feature.base import FeatureManager

DEFAULT = 100000

class IndexSort(Model):

    features_to_weights: Dict[str, float]

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

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

        if "features" in kwargs:
            name_to_features = kwargs["features"]

        name_to_reverse = {}
        if "reverse" in kwargs:
            name_to_reverse = kwargs["reverse"]

        name_to_negative = {}
        if "negative" in kwargs:
            name_to_negative = kwargs["negative"]

        # a function for compare PE liked value
        def negative_cmp(x, y):
            if x[1] * y[1] < 0:
                if x[1] > 0:
                    return -1
                else:
                    return 1
            if x[1] < 0 and y[1] < 0:
                if x[1] < y[1]:
                    return 1
            if x[1] > y[1]:
                return 1
            return -1

        name_to_idx = {}
        for k, v in name_to_features.items():
            rev = name_to_reverse.get(k, False)
            negative = name_to_negative.get(k, False)
            if negative:
                tmp = sorted(v.items(), key=cmp_to_key(negative_cmp), reverse=rev)
            else:
                tmp = sorted(v.items(), key=lambda x: x[1], reverse=rev)
            print(k, tmp)
            name_to_idx[k] = {tmp[i][0]: i for i in range(len(tmp))}
        #print(name_to_idx)

        result = {}
        for i in stocks:
            ret = self.policy(name=i, name_to_features=name_to_idx)
            if ret and ret != None:
                result[i] = ret
        # print(result)
        return result

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
            #print(k, v, name)
            if name in v:
                result += self.features_to_weights[k] * v[name]
            else:
                result += self.features_to_weights[k] * (len(v))
        if result != DEFAULT:
            return result - DEFAULT
        else: 
            return 