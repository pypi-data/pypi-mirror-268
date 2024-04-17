import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.database.storage.china.macro import (
    gdp,
    pmi,
    ppi,
    lpr,
    money_supply,
    cpi,
    consumer_faith,
    treasury_bond_yield,
    international_trade
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
            "t_macro_" + func.__name__,
            {
                "TIME": VARCHAR(32),
                "DATE": VARCHAR(32)
            },
            single=True
            )
        idx += 1
    except:
        print(func.__name__, idx)
    if init:
        db.execute("alter table t_macro_" + func.__name__ + " add PRIMARY KEY(`TIME`)")

def build_marco():

    call_func(gdp)
    # alter table t_macro_gdp add PRIMARY KEY(`TIME`);

    call_func(pmi)
    # alter table t_macro_pmi add PRIMARY KEY(`TIME`);

    call_func(ppi)
    # alter table t_macro_ppi add PRIMARY KEY(`TIME`);

    call_func(lpr)
    # alter table t_macro_lpr add PRIMARY KEY(`TIME`);

    call_func(money_supply)
    # alter table t_macro_money_supply add PRIMARY KEY(`TIME`);

    call_func(cpi)
    # alter table t_macro_cpi add PRIMARY KEY(`TIME`);

    call_func(consumer_faith)
    # alter table t_macro_consumer_faith add PRIMARY KEY(`TIME`);

    call_func(treasury_bond_yield)
    # alter table t_macro_treasury_bond_yield add PRIMARY KEY(`DATE`);

    call_func(international_trade)
    
if __name__== "__main__":
    build_marco()