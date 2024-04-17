import numpy as np

from openfinance.strategy.operator.base import Operator

try:
    from talib.abstract import *
    
    class OnBalanceVolume(Operator):
        name:str = "OBV"

        def run(
            self,
            data,
            **kwargs
        ):
            """
                Function to evaluate specific stocks
            """

            latest = kwargs.get("latest", True)

            obv = OBV(
                np.array(data["close"]),
                np.array(data["volume"])
            )
            if latest:
                return obv[-1]
            
            return obv 

except Exception as e:
    
    from openfinance.datacenter.database.quant.call import get_factor_process
    
    class OnBalanceVolume(Operator):
        name:str = "OBV"

        def run(
            self,
            data,
            **kwargs
        ):
            """
                Function to evaluate specific stocks
            """
            # print(data)
            data = {k: v.tolist() for k, v in data.items()}
            latest = kwargs.get("latest", True)
            obv = get_factor_process(
                factor=self.name,
                quant_data=data
            )
            if latest:
                return obv[-1]
            
            return obv