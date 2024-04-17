import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.strategy.feature.base import FeatureManager
from openfinance.datacenter.database.source.eastmoney.trade import index_member
from openfinance.datacenter.database.source.eastmoney.util import get_current_date


stock_code = index_member('上证50')
DATE = get_current_date()
db = DataBaseManager(Config()).get("quant_db")
# print(db.exec("show databases"))

def init_table():
    db.create_table(
        table = "t_stock_feature_map",
        contents = {
            "SECURITY_NAME": "varchar(16)",
            "SECURITY_CODE": "varchar(16)",        
            "fid": "int",
            "val": "double",
            "fname": "varchar(32)",
            "TIME": "varchar(16)"
        }
    )

    db.exec("alter table t_stock_feature_map add PRIMARY KEY(`SECURITY_NAME`, `fid`)")


def store_company_features(init=False):
    if init:
        init_table()    
    code_list = stock_code['股票代码'].tolist()
    name_list = stock_code['股票名称'].tolist()
    # for (k, v) in [("PricePosition", FeatureManager().get("PricePosition"))]:
    FeatureManager().name_to_features.clear()
    try:
        import openfinance.strategy.feature.company
    except:
        pass
    for k, v in FeatureManager().name_to_features.items():
        # print(k)
        result = v.run(candidates=name_list).get("result")
        # print(result)
        for i in range(len(name_list)):
            val = result.get(name_list[i], 0)
            data = {
                "SECURITY_NAME": name_list[i],
                "SECURITY_CODE": code_list[i],        
                "fid": v.fid,
                "val": val,
                "fname": v.name,
                "TIME": DATE            
            }
            db.insert(
                "t_stock_feature_map",
                data,
                dup_key = ["val", "TIME"]
            )
if __name__== "__main__":
    store_company_features(init=False)
    #pass