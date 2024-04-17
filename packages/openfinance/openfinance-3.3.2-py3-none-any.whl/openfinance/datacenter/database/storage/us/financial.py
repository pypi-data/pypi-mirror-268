import time
from sqlalchemy.types import VARCHAR

from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager

from openfinance.datacenter.database.storage.us.base import (
    get_all_stock,
    financial_statement
)

db = DataBaseManager(Config()).get("db")


def store_financial_statement(init=False):
    idx = 0
    for k in get_all_stock():
        try:
            data = financial_statement(k[2])
            #print(idx, k, v)
            time.sleep(0.5)
            db.insert_data_by_pandas(
                data, 
                "t_us_stock_financial_statement",
                {
                    "SECURITY_NAME": VARCHAR(64),
                    "DATE": VARCHAR(16),
                    "DATE_TYPE": VARCHAR(8)            
                },
                single=True
                )
            idx += 1
            #if idx == 3:
            #    break
        except Exception as e:
            print(e, k)
            continue
    if init:
        db.execute("alter table t_us_stock_financial_statement add PRIMARY KEY(`SECURITY_NAME`, `DATE`, `DATE_TYPE`)")


if __name__ == '__main__':
    store_financial_statement(init=True)