import datetime
import numpy as np
from typing import (
    List,
    Any,
    Dict
)

from openfinance.datacenter.database.source.eastmoney.trade import multiday_moneyflow

from openfinance.strategy.feature.base import Feature

NO_DIVIDENT = -100000

class MoneyFlowDirect(Feature):
    name = "MoneyFlowDirect"
    def _user_source(
        self,
        name
    ):
        try:
            return multiday_moneyflow(name)["主力净流入占比"]
        except:
            return None