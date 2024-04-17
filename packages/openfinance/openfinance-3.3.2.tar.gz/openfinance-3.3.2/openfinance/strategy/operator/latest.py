import numpy as np

from openfinance.strategy.operator.base import Operator

class Latest(Operator):
    name:str = "Latest"

    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        if isinstance(data, list): # db select format
            if isinstance(data[-1], tuple):
                return data[-1][-1]
            return data[-1]
        return data