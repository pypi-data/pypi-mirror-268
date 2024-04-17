import numpy as np

from openfinance.strategy.operator.base import Operator

class Acc(Operator):
    name:str = "Acc"

    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        period = kwargs.get("period", 4)
        v = []
        if True:        
            for d in data[-period:]:
                if d != None:
                    v.append(d[1])
        else:
            v = data[-period:]
        slope = np.mean(np.diff(v))
        return slope