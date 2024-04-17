import datetime
import numpy as np
from typing import (
    List,
    Any,
    Dict
)


from openfinance.config import Config
from openfinance.strategy.feature.base import Feature
from openfinance.strategy.operator.base import OperatorManager


NO_DIVIDENT = -100000

class DividentSpeed(Feature):
    name = "DividentSpeed"
    def eval(
        self,
        *args,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        data = kwargs.get("data")
        # print(data)
        data = {int(k[1][:4]): k[0] for k in data}
        #print(data)
        oldyear = max(data.keys())
        lastyear = datetime.date.today().year - 1
        latestyear = max(oldyear, lastyear)
        v = []
        
        for i in range(latestyear - 2, latestyear + 1, 1):
            if i in data and data[i] != None:
                v.append(data[i])
            else:
                v.append(0)
        # print(v)
        total = sum(v)
        if total:
            slope = np.mean(np.diff(v))
            return slope
        else:
            return NO_DIVIDENT