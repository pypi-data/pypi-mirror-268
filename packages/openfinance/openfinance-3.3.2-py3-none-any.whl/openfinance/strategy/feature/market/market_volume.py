import datetime
import numpy as np
from typing import (
    List,
    Any,
    Dict
)

from openfinance.datacenter.database.source.eastmoney.util import get_previous_date
from openfinance.datacenter.database.source.eastmoney.trade import quant_data

from openfinance.strategy.feature.base import Feature

NO_DIVIDENT = -100000
DATE = get_previous_date(300).replace("-","")

class MarketVolume(Feature):
    name = "MarketVolume"
    def _user_source(
        self,
        name
    ):
        try:
            data = quant_data("上证指数",  start=DATE, freq='d', fqt=2)
            dates = data.pop("date")
            return {"data": data, "date": dates}
        except:
            return None