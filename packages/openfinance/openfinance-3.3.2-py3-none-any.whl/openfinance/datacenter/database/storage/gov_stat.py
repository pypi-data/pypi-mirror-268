import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager

from openfinance.datacenter.database.source.gov.stat import *

db = DataBaseManager(Config()).get("db")

def store_gov_stat(
    cur_date = '202311',
    dbcode = "hgyd",
    init=False
):
    idx = 0

    try:
        data = get_gov_stat_df(cur_date=cur_date, dbcode=dbcode)

        col_names = data.columns.tolist()
        col_names_dict = dict()
        for key in col_names:
            col_names_dict[key] = "Date" + key

        print(col_names)
        data.rename(columns=col_names_dict, inplace=True)
        
        time.sleep(0.5)
        db.insert_data_by_pandas(
            data, 
            "t_gov_stat_" + dbcode,
            dtypes={},
            if_exists='replace',
            single=False                
            )
        idx += 1
    except:
        print("error: ", dbcode)

if __name__== "__main__":
    print("build gov stat")
    store_gov_stat('202311', 'hgyd')
