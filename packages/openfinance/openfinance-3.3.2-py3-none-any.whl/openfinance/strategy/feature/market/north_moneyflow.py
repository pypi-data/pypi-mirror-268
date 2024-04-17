import datetime
import numpy as np
from typing import (
    List,
    Any,
    Dict
)

from openfinance.datacenter.database.source.eastmoney.market import (
    north_money_flow,
)

from openfinance.strategy.feature.base import Feature

NO_DIVIDENT = -100000

class NorthMoneyFlowVar(Feature):
    name = "NorthMoneyFlowVar"
    def _user_source(
        self,
        name
    ):
        try:
            data = north_money_flow()            
            data["time"] = data.pop("DATE")
            data["data"] = data.pop("VOLUME")
            return data
        except:
            return None