from typing import (
    List,
    Any,
    Dict,
    Union
)
import json
from abc import ABC, abstractmethod
from pydantic import BaseModel, root_validator

from openfinance.utils.singleton import singleton
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager

from openfinance.datacenter.knowledge.entity_graph import EntityGraph
from openfinance.strategy.operator.base import OperatorManager
from openfinance.strategy.feature.data_adaptor import DataAdaptor

db = DataBaseManager(Config()).get("quant_db")

class Feature(BaseModel):
    name: str = ""
    fid: int = 0
    desc: str = ""
    source: Dict[str, Any] = {}
    operator: Dict[str, Any] = {}

    @classmethod
    def from_source(
        cls,
        *args,
        **kwargs
    ) -> "Feature":
        return cls(
            name=kwargs.get("name"),
            fid=kwargs.get("id"),
            desc=kwargs.get("desc"),
            source=kwargs.get("source", {}),
            operator=kwargs.get("operator", {})
        )

    def update(
        self,
        feature: Any
    ) -> None:
        self.name = feature.name
        self.fid = feature.fid
        self.desc = feature.desc
        self.source = feature.source
        self.operator = feature.operator

    def run(
        self,
        *args,
        **kwargs
    ):
        """
            Function to run all stocks
            data: {
                "name": {
                    "time": [],
                    "data": []
                }
            }
        """
        candidates = kwargs.get("candidates", list(EntityGraph().companies.keys()))
        if kwargs.get("from_db", False):          
            data_adaptor = DataAdaptor().get(kwargs.get("type", ""))
            data, keys = data_adaptor(candidates, fid=self.fid)
            if self.operator.get("latest", False) or kwargs.get("latest", False):
                new_result = {k: v[-1] for k, v in data.items()}
                new_key = {k: v[-1] for k, v in keys.items()}
                return {"result": new_result, "TIME": new_key}
            return {"result": data, "TIME": keys}   
        else:
            data_adaptor = DataAdaptor().get(self.source.get("type", ""))            
            if data_adaptor:
                data = data_adaptor(candidates, **self.source)
            else:
                if isinstance(candidates, str):
                    candidates = [candidates]     
                data = {}
                for name in candidates:
                    data[name] = self._user_source(name)
            
            result = {}
            key = {}
            for name, d in data.items():
                # print(data)
                if isinstance(d, dict) and self.source.get("key", "") in d:
                    k = d[self.source.get("key", "")]
                    key[name] = k            
                if isinstance(d, dict) and "data" in d:
                    d = d["data"]                
                result[name] = self.eval(name=name, data=d)
            return {"result": result, self.source.get("key", ""): key}

    def _user_source(
        self,
        name
    ):
        pass

    # @abstractmethod
    def eval(
        self,
        *args,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        data = kwargs.get("data")
        op = self.operator.get("name", "")
        if OperatorManager().get(op):
            return OperatorManager().get(op)(data, **self.operator)
        return data

    def fetch(
        self,
        *args,
        **kwargs
    ) -> List[Any]:
        """
            Function to filter candidates with restrictions
            mode: "lt le eq ge gt in"
        """
        # print(kwargs)
        thresh = kwargs.get("thresh", 0)
        mode = kwargs.get("mode", "gt")
        if kwargs.get("from_db", False):
            range_str = f"fid={self.fid}"
            if mode == "gt":
                range_str += f" and val>{thresh}"
            elif mode == "lt":
                range_str += f" and val<{thresh}"                
            elif mode == "in":
                pass
            data = db.select_more(
                "t_stock_feature_map",
                range_str=range_str,
                field="SECURITY_NAME,val"
            )
            # print(data)
            result = {}
            for d in data:
                result[d["SECURITY_NAME"]] = d["val"]
            return result
        else:
            data = self.run().get("result")
            if mode == "gt":
                return dict(filter(lambda x: x[1] > thresh, data.items()))
            elif mode == "lt":
                return dict(filter(lambda x: x[1] < thresh, data.items()))
            elif mode == "in":
                return # to do

@singleton
class FeatureManager:
    name_to_features: Dict[str, Feature] = {}

    def _add(
        self, 
        feature: Feature 
    ) -> None:
        try:
            if feature.name not in self.name_to_features:
                self.name_to_features.update({feature.name: feature})
            else:
                self.name_to_features[feature.name].update(feature)
        except Exception as e:
            raise e

    def register(
        self, 
        feature : Union[List[Feature], Feature, Dict[str, Any]]
    ) -> None:
        
        if isinstance(feature, list):
            for i in feature:
                self._add(i())
        elif isinstance(feature, dict):
            self._add(
                Feature.from_source(**feature)
            )
        else:
            self._add(feature())

    def register_from_file(
        self,
        file: str
    ):
        with open(file, "r") as infile:
            jsondata = json.load(infile)
            for d in jsondata["data"]:
                self.register(d)

    def get(
        self, 
        name: str
    ):
        if name in self.name_to_features:
            return self.name_to_features[name]
        return None