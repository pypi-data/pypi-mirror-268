import datetime
import numpy as np
from typing import (
    List,
    Any,
    Dict
)


from openfinance.config import Config
from openfinance.strategy.feature.base import Feature
from openfinance.strategy.operator.base import OperatorManager


NO_DIVIDENT = -100000

class NewsSentiment(Feature):
    name = "NewsSentiment"
    def eval(
        self,
        *args,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        result = 0
        data = kwargs.get("data")
        if len(data):
            # print(data)
            data = data[0]
            days = data.split(",")
            for d in days:
                s = d.split(":")
                result += int(s[0]) * 2
                result += int(s[1])
                result -= int(s[2]) 
        return result