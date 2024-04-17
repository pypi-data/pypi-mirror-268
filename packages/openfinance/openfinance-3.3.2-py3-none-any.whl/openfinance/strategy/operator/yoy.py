import numpy as np

from openfinance.strategy.operator.base import Operator

class Yoy(Operator):
    name:str = "Yoy"

    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        period = kwargs.get("period", 5)
        # print(data)
        if (len(data)>4):
            return data[-1] / (data[-5] + 0.000001)