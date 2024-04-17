import numpy as np

from openfinance.strategy.operator.base import Operator

try:
    from talib.abstract import *

    class MAConDiv(Operator):
        name:str = "MACD"

        def run(
            self,
            data,
            **kwargs
        ):
            """
                Function to evaluate specific stocks
            """
            fastperiod = kwargs.get("fastperiod", 12)
            slowperiod = kwargs.get("slowperiod", 26)
            signalperiod = kwargs.get("signalperiod", 9)
            latest = kwargs.get("latest", True)

            if isinstance(data, list):
                macd, macdsignal, macdhist = MACD(
                    np.array(data, dtype='double'), 
                    fastperiod, 
                    slowperiod, 
                    signalperiod
                )
            if latest:
                return macdhist[-1]
            
            return macdhist    
except Exception as e:

    from openfinance.datacenter.database.quant.call import get_factor_process

    class MAConDiv(Operator):
        name:str = "MACD"

        def run(
            self,
            data,
            **kwargs
        ):
            """
                Function to evaluate specific stocks
            """
            fastperiod = kwargs.get("fastperiod", 12)
            slowperiod = kwargs.get("slowperiod", 26)
            signalperiod = kwargs.get("signalperiod", 9)
            latest = kwargs.get("latest", True)

            if isinstance(data, list):
                macdhist = get_factor_process(
                    factor=self.name,
                    quant_data=data
                )
            if latest:
                return macdhist[-1]
            
            return macdhist      