import numpy as np

from openfinance.strategy.operator.base import Operator

class Hist(Operator):
    name:str = "Hist"

    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        latest = kwargs.get("high", True)            
        thresh = kwargs.get("thresh", 1)
        assert len(data) > 0, "data is empty"
        count = 0
        for i in data:
            if i <= thresh:
                count += 1
        return count/len(data)
