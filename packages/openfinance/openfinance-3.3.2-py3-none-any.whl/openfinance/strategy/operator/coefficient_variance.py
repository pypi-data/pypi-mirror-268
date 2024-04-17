import numpy as np

from openfinance.strategy.operator.base import Operator

def tanh(x):
    return 2./(1. + np.exp(-2*x)) - 1

def sigmoid(x):
    return 1./(1. + np.exp(-x))

class CoeffVar(Operator):
    name:str = "CoeffVar"

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
                nd = np.array(data[i-window:i], dtype='double')
                # div = np.mean(abs(nd)) * np.sign(sum(nd))             
                result.append(np.std(nd, ddof=1)/np.mean(abs(nd)))
                # result.append((np.std(nd, ddof=1)))
        if latest:
            return result[-1]
        return result