import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.database.storage.fred.base import fred_balance_sheet
from openfinance.datacenter.database.storage.fred.base import us_government_fiscal

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
            "t_us_" + func.__name__,
            {
                "DATE": VARCHAR(32)
            },
            single=False
            )
        idx += 1
    except:
        print(func.__name__, idx)
    if init:
        db.execute("alter table t_us_" + func.__name__ + " add PRIMARY KEY(`DATE`)")

def build_fed():
    call_func(fred_balance_sheet)
    # alter table t_us_fred_balance_sheet add PRIMARY KEY(`DATE`);
    call_func(us_government_fiscal)
    # alter table t_us_us_government_fiscal add PRIMARY KEY(`DATE`);    