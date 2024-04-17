import numpy as np

from openfinance.strategy.operator.base import Operator

class Mean(Operator):
    name: str = "Mean"

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
                    v.append(d)
        else:
            v = data[-period:]
        # print(kwargs, v)
        slope = np.mean(v)
        return slope