import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager

from openfinance.datacenter.database.storage.china.market import (
    market_loan_money
)

db = DataBaseManager(Config()).get("db")


def call_func(
    func,
    init=False    
):
    idx = 0
    try:
        data = func()
        time.sleep(0.5)
        db.insert_data_by_pandas(
            data, 
            "t_" + func.__name__,
            {
                "DATE": VARCHAR(32)
            },
            single=True
            )
        idx += 1
    except:
        print(func.__name__, idx)
    if init:
        db.execute("alter table t_" + func.__name__ + " add PRIMARY KEY(`DATE`)")

def build_market():
    call_func(market_loan_money)

if __name__== "__main__":
    build_market()
    # alter table t_market_loan_money add PRIMARY KEY(`DATE`);