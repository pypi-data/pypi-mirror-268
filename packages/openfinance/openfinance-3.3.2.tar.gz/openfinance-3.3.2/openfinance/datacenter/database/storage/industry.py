import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager

from openfinance.datacenter.database.storage.china.industry import *

config = Config()
db = DataBaseManager(Config()).get("db")

def store_north_money_to_sector(
    date = [None],
    init=False
):
    idx = 0
    for v in date:
        try:
            data = north_money_to_sector(v)
            print(idx, v)
            time.sleep(0.5)
            db.insert_data_by_pandas(
                data, 
                "t_industry_north_money_to_sector",
                {
                    "INDUSTRY_NAME": VARCHAR(16),
                    "DATE": VARCHAR(32),
                    "INTERVAL_TYPE": VARCHAR(8)
                },
                single=True                
                )
            idx += 1
        except:
            print(v, idx)
            continue
    if init:
        db.execute("alter table t_industry_north_money_to_sector add PRIMARY KEY(`INDUSTRY_NAME`, `INTERVAL_TYPE`)")

def store_industy_all_valuation(
    init=False
):
    try:
        data = industy_all_valuation()
        time.sleep(0.5)
        db.insert_data_by_pandas(
            data, 
            "t_industy_all_valuation",
            {
                "INDUSTRY_NAME": VARCHAR(16),
            },
            single=True                
            )

    except Exception as e:
        print(e)
    if init:
        db.execute("alter table t_industy_all_valuation add PRIMARY KEY(`INDUSTRY_NAME`)")


if __name__== "__main__":
    print("build industry")
    store_north_money_to_sector(["2023-09-06"])
    store_industy_all_valuation(init=True)
    #alter table t_industry_north_money_to_sector add PRIMARY KEY(`INDUSTRY_NAME`, `INTERVAL_TYPE`);