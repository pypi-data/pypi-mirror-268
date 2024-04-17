import numpy as np

from openfinance.strategy.operator.base import Operator


NO_DIVIDENT = -100000

class LatestPosition(Operator):
    name:str = "LatestPosition"

    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        latest = kwargs.get("latest", True)            
        result = []
        if isinstance(data, list): # db select format
            window = kwargs.get("window", len(data))
            assert len(data) > window, f"data is shorter than {window}"
            result += [0] * (window - 1)
            for i in range(window, len(data)):
                idx = 0
                r = data[i]
                for d in data[i-window:i]:
                    if d > r:
                        idx += 1
                result.append(idx + 1)
        
        if latest:
            return result[-1]

        return result