import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.database.storage.national_data.base import government_debt
from openfinance.datacenter.database.storage.national_data.base import local_government_debt

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
            "t_china_" + func.__name__,
            {
                "TIME": VARCHAR(32)
            },
            single=False
            )
        idx += 1
    except:
        print(func.__name__, idx)
    if init:
        db.execute("alter table t_china_" + func.__name__ + " add PRIMARY KEY(`TIME`)")

def build_debt():
    call_func(government_debt)
    # alter table t_china_government_debt add PRIMARY KEY(`TIME`);    
    call_func(local_government_debt)
    # alter table t_china_local_government_debt add PRIMARY KEY(`TIME`);