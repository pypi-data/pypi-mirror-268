import datetime
import numpy as np
from typing import (
    List,
    Any,
    Dict
)

from openfinance.datacenter.database.source.eastmoney.trade import web_data

from openfinance.config import Config
from openfinance.strategy.feature.base import Feature
from openfinance.strategy.operator.base import OperatorManager


NO_DIVIDENT = -100000

class WinCostDist(Feature):
    name = "WinCostDist"
    def _user_source(
        self,
        name
    ):
        try:
            return web_data(name, start="20211231")
        except:
            return None
    
    def eval(
        self,
        *args,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        result = 0
        name = kwargs.get("name")
        data = kwargs.get("data", None)
        #print(data)
        chip = {}
        def calc_by_mean(
            high,
            low,
            vol,
            turnover,
            div,
            A
        ):
            minD = (high - low)/div
            x = [round(low + i * minD, 2) for i in range(div)]
            #print(x)
            minVol = vol/div
            for k,v in chip.items():
                chip[k] = chip[k] * (1 - turnover/100 * A)
            for i in x:
                if i in chip:
                    chip[i] += minVol * turnover/100 * A
                else:
                    chip[i] = minVol * turnover/100 * A
        def win_rate(
            price
        ):
            total = 0.000001
            win = 0
            for k, v in chip.items():
                total += v
                if k < price:
                    win += v
            return win/total

        if len(data):
            last_price = data.iloc[len(data)-1]['close']
            for i in range(len(data)):
                d = data.iloc[i]
                calc_by_mean(d['high'],d['low'],d['volume'],d['turnover_rate'], 10, 1)
            result = win_rate(last_price)
        #print(chip)
        return result