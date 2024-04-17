import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.strategy.feature.base import FeatureManager
from openfinance.datacenter.database.source.eastmoney.util import get_current_date

DATE = get_current_date()
db = DataBaseManager(Config()).get("quant_db")
# print(db.exec("show databases"))
NAME = "上证指数"

def init_table():
    db.create_table(
        table = "t_market_feature_map",
        contents = {     
            "fid": "int",
            "val": "double",
            "fname": "varchar(32)",
            "TIME": "varchar(16)"
        }
    )

    db.exec("alter table t_market_feature_map add PRIMARY KEY(`TIME`, `fid`)")


def store_market_features(init=False):
    if init:
        init_table()
    name_list = [NAME]
    FeatureManager().name_to_features.clear()
    try:
        import openfinance.strategy.feature.market
    except:
        pass        
    for k, v in FeatureManager().name_to_features.items():
    # for (k, v) in [("HighestRatio", FeatureManager().get("HighestRatio"))]:
        # print(k)
        result = v.run(candidates=name_list)
        # print(result)
        vals = result.pop("result")[NAME]
        if isinstance(vals, list):
            # print(result)
            keys = list(result.values())[0][NAME]
            for i in range(1, len(vals) + 1, 1):
                data = {    
                    "fid": v.fid,
                    "val": vals[-i],
                    "fname": v.name,
                    "TIME": keys[-i]     
                }
                db.insert(
                    "t_market_feature_map",
                    data,
                    dup_key = ["val, fname"]
                )            
        else:
            data = {    
                "fid": v.fid,
                "val": vals,
                "fname": v.name,
                "TIME": DATE            
            }
            db.insert(
                "t_market_feature_map",
                data,
                dup_key = ["val", "fname"]
            )
if __name__== "__main__":
    store_market_features(init=False)
    #pass