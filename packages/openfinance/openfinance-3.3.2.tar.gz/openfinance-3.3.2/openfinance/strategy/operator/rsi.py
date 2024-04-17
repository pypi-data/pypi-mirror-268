import numpy as np

from openfinance.strategy.operator.base import Operator

try:
    from talib.abstract import *

    class RSI(Operator):
        name:str = "RSI"

        def run(
            self,
            data,
            **kwargs
        ):
            """
                Function to evaluate specific stocks
            """
            latest = kwargs.get("latest", True)
            rsi = RSI(np.array(data, dtype='double'))
            if latest:
                return rsi[-1]
            return rsi

except Exception as e:
    
    from openfinance.datacenter.database.quant.call import get_factor_process

    class RSI(Operator):
        name:str = "RSI"

        def run(
            self,
            data,
            **kwargs
        ):
            """
                Function to evaluate specific stocks
            """
            latest = kwargs.get("latest", True)

            rsi = get_factor_process(
                factor=self.name,
                quant_data=data
            )

            if latest:
                return rsi[-1]
            return rsi



