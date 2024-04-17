import numpy as np

from openfinance.strategy.operator.base import Operator


NO_DIVIDENT = -100000

class DivideLatest(Operator):
    name:str = "DivideLatest"

    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """        
        latestdata = data[-1]
        try:
            if len(latestdata) == 2:
                return latestdata[1]/latestdata[0]
        except:
            print(data)
        return NO_DIVIDENT