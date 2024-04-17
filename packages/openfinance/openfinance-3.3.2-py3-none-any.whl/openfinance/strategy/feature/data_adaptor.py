from typing import (
    List,
    Any,
    Dict,
    Union,
    Callable
)
import json
from abc import ABC, abstractmethod
from pydantic import BaseModel, root_validator

from openfinance.utils.singleton import singleton
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.database.source.eastmoney.trade import (
    stock_realtime,
    market_realtime
)
from openfinance.datacenter.knowledge.entity_graph import EntityGraph
from openfinance.strategy.operator.base import OperatorManager

db = DataBaseManager(Config()).get("db")
quant_db = DataBaseManager(Config()).get("quant_db")

@singleton
class DataAdaptor:
    """
        Translate different sources to standard format datatype
        {
            "name": {
                "time": []
                "data": []
            }
        }
    """
    name: str = "adaptor"
    name_to_sources: Dict[str, Callable] = {}

    def add(
        self, 
        name: str,
        func: Callable 
    ) -> None:
        try:
            if name not in self.name_to_sources:
                self.name_to_sources.update({name: func})
            else:
                self.name_to_sources[name].update(func)
        except Exception as e:
            raise e

    def get(
        self, 
        name: str
    ):
        if name in self.name_to_sources:
            return self.name_to_sources[name]
        return None


def _realtime(
    candidates,
    **kwargs
):
    if isinstance(candidates, str):
        candidates = [candidates]
    # print(candidates)
    pd = stock_realtime(candidates)            
    
    result = {}
    for i in range(len(pd)):
        d = pd.iloc[i]
        result[d[kwargs["key"]]] = d[kwargs["value"]]
    return result

DataAdaptor().add("realtime", _realtime)

def _db_obj(
    candidates,
    **kwargs
):
    obj = kwargs.get("obj", "SECURITY_NAME")
    if candidates:
        if len(candidates) > 1:
            range_str = f"{obj} in ('" + "','".join(candidates) + "')"
        else:
            range_str = f"{obj}='" + candidates[0] + "'"
    else:
        range_str = ""

    data = db.select_more(
        table = kwargs["table"],
        range_str = range_str,
        field = kwargs["field"]
    )

    # groupby and only consider single value case , to update later
    name_to_sources = {}
    if isinstance(kwargs["value"], str):
        for i in data:
            if i[kwargs["value"]] is None:
                continue
            if i[obj] in name_to_sources:
                name_to_sources[i[obj]][i[kwargs["key"]]] = i[kwargs["value"]]
            else:
                name_to_sources[i[obj]] = {i[kwargs["key"]]: i[kwargs["value"]]}
    elif isinstance(kwargs["value"], list): # case for multi value
        for i in data:
            if i[obj] in name_to_sources:
                new_val = [i[j] for j in kwargs["value"]]
                name_to_sources[i[obj]][i[kwargs["key"]]] = new_val
            else:
                new_val = [i[j] for j in kwargs["value"]]
                name_to_sources[i[obj]] = {i[kwargs["key"]]: new_val}            

    result = {}
    for k, v in name_to_sources.items():
        #print(k, v)        
        v = sorted(v.items(), key=lambda x:x[0])
        dates = [x[0] for x in v]
        values = [x[1] for x in v]
        result[k] = {
            kwargs["key"]: dates,
            "data": values
        }
    return result

DataAdaptor().add("db", _db_obj)

def _db_all(
    candidates,
    **kwargs
):
    if isinstance(candidates, list):
        candidates = candidates[0]
    range_str = kwargs.get("filter", "")
    data = db.select_more(
        table = kwargs["table"],
        range_str = range_str,
        field = kwargs["field"]
    )

    # groupby and only consider single value case , to update later
    key_to_features = {}
    if isinstance(kwargs["value"], str):
        for i in data:
            if i[kwargs["value"]] is None:
                continue
            key_to_features[i[kwargs["key"]]] = i[kwargs["value"]]
    elif isinstance(kwargs["value"], list): # case for multi value
        for i in data:
            new_val = [i[j] for j in kwargs["value"]]
            key_to_features[i[kwargs["key"]]] = new_val          

    v = sorted(key_to_features.items(), key=lambda x:x[0])
    dates = [x[0] for x in v]
    values = [x[1] for x in v]
    return {
        candidates: {
            kwargs["key"]: dates,
            "data": values
        }
    }

DataAdaptor().add("db_all", _db_all)

def _company(
    candidates,
    fid,
    **kwargs
):
    data = quant_db.select_more(
        "t_stock_feature_map",
        range_str=f"fid={fid}"
    )
    # print(data)
    result = {}
    keys = {}
    for d in data:
        # print(d)
        if d["SECURITY_NAME"] in candidates:
            result[d["SECURITY_NAME"]] = d["val"]
            keys[d["SECURITY_NAME"]] = d["TIME"]
    return result, keys

DataAdaptor().add("company", _company)


def _market(
    candidates,
    fid,
    **kwargs
):
    if isinstance(candidates, list):
        candidates = candidates[0]

    data = quant_db.select_more(
        "t_market_feature_map",
        range_str=f"fid={fid} order by TIME"
    )
    # print(data)
    result = []
    keys = []
    for d in data:
        result.append(d['val'])
        keys.append(d['TIME'])
    return {candidates: result}, {candidates: keys}

DataAdaptor().add("market", _market)