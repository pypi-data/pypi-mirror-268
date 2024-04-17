import numpy as np

from openfinance.strategy.operator.base import Operator

class MovingAverage(Operator):
    name: str = "MovingAverage"

    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        
        window = kwargs.get("window", 5)
        latest = kwargs.get("latest", True)

        result = 0
        #print(data)
        slope = np.convolve(
            np.array(data, dtype='double'), np.ones(window), "valid") / window
        # print(",".join(map(str, slope)))
        # Or 
        # return SMA(np.array(data, dtype='double'), window)
        if latest:
            return slope[-1]
        return slope