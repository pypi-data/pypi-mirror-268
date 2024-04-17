import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.database.source.eastmoney.trade import (
    web_data,
    stock_code_dict,
    index_member
)
from openfinance.datacenter.database.source.eastmoney.util import get_previous_date

config = Config()
db = DataBaseManager(Config()).get("quant_db")
# print(db.exec("show databases"))
DATE = get_previous_date(90).replace("-", "")

stock_code = index_member('上证50')
names = {
    "name": "SECURITY_NAME",
    "date": "DATE"
}
def store_quant_data(init=False):
    idx = 0
    for i in range(len(stock_code)):
        try:
            k = stock_code.iloc[i]['股票名称']
            data = web_data(k, start=DATE)
            data = data.rename(columns=names)
            time.sleep(0.5)
            db.insert_data_by_pandas(
                data, 
                "t_basic_daily_kline",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "DATE": VARCHAR(32),              
                },
                single=True
                )
            idx += 1
            #if idx == 3:
            #    break
        except:
            print(stock_code.iloc[i])
            continue
    if init:
        db.execute("alter table t_basic_daily_kline add PRIMARY KEY(`SECURITY_NAME`, `DATE`)")
    else:
        db.execute(f'delete from t_basic_daily_kline where DATE < {DATE}')

if __name__== "__main__":
    store_quant_data()
    #pass