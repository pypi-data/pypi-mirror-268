import pandas
import time
from openfinance.config import Config
from sqlalchemy.types import VARCHAR
from openfinance.datacenter.database.base import DataBaseManager

from openfinance.datacenter.database.storage.china.stock import ( 
    financial_report_statement,
    balance_sheet_statement,
    income_profit_statement,
    cashflow_statement,
    stock_holder_num,
    stock_code_dict,
    main_business,
    forcast_report,
    eps_forecast,
    stock_divide,
    daily_money_flow
)

db = DataBaseManager(Config()).get("db")

stock_code = stock_code_dict()

#stock_code = {"贵州茅台":1}
# done
"""
def store_indictor():
    idx = 0
    for k, v in stock_code.items():
        try:
            data = stock_indicator(v)
            print(idx, k, v)
            time.sleep(0.5)
            data["name"] = k
            data["code"] = v
            db.insert_data_by_pandas(
                data, 
                "t_stock_indicator_sina", 
                {
                    "name": VARCHAR(16),
                    "date": VARCHAR(16)
                }         
                )
            idx += 1
        except:
            print(k, v, idx)
            continue
"""

def store_main_business(init=False):
    idx = 0
    for k, v in stock_code.items():
        try:
            data = main_business(k)
            #print(idx, k, v)
            time.sleep(0.5)
            data["SECURITY_NAME"] = k
            data["SECURITY_CODE"] = v
            db.insert_data_by_pandas(
                data, 
                "t_main_business_f10",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "DATE": VARCHAR(32),
                    "CATEGORY": VARCHAR(32),
                    "DIRECTION": VARCHAR(32),                  
                },
                single=True
                )
            idx += 1
            #if idx == 3:
            #    break
        except:
            print(k, v, idx)
            continue
    if init:
        db.execute("alter table t_main_business_f10 add PRIMARY KEY(`SECURITY_NAME`, `DATE`, `DIRECTION`, `CATEGORY`)")

def store_financial_report_statement(
    latest=True,
    init=False
):
    idx = 0
    for k, v in stock_code.items():
        idx += 1
        try:      
            data = financial_report_statement(v, latest=latest)
            #print(idx, k, v)
            time.sleep(0.5)
            #data["name"] = k
            #data["code"] = v
            db.insert_data_by_pandas(
                data, 
                "t_financial_report_statement",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "DATE": VARCHAR(16)
                },
                single=True                
                )
        except:
            print(k, v, idx)
            continue
    if init:
        db.execute("alter table t_financial_report_statement add PRIMARY KEY(`SECURITY_NAME`, `DATE`)")

def store_balance_sheet(
    latest=True,
    init=False
):
    idx = 0
    for k, v in stock_code.items():
        try:
            idx += 1
            data = balance_sheet_statement(v, latest=latest)
            print(idx, k, v)
            time.sleep(0.5)
            #data["name"] = k
            #data["code"] = v
            db.insert_data_by_pandas(
                data, 
                "t_balance_sheet_statement",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "SECURITY_CODE": VARCHAR(16),                  
                    "DATE": VARCHAR(32)
                },
                single=True                
                )
        except:
            print(k, v, idx)
            continue
    if init:
        db.execute("alter table t_balance_sheet_statement add PRIMARY KEY(`SECURITY_NAME`, `DATE`)")

def store_income_profit(
    latest=True,
    init=False
):
    idx = 0
    for k, v in stock_code.items():
        try:
            data = income_profit_statement(v, latest=latest)
            print(idx, k, v)
            time.sleep(0.5)
            #data["name"] = k
            #data["code"] = v
            db.insert_data_by_pandas(
                data, 
                "t_income_profit_statement",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "DATE": VARCHAR(32),
                    "SECURITY_CODE": VARCHAR(16)
                },
                single=True                
                )
            idx += 1
        except:
            print(k, v, idx)
            continue
    if init:
        db.execute("alter table t_income_profit_statement add PRIMARY KEY(`SECURITY_NAME`, `DATE`)")

def store_cash_flow(
    date = [None],
    init=False
):
    idx = 0
    for v in date:
        try:
            data = cashflow_statement(v)
            print(idx, v)
            time.sleep(0.5)
            db.insert_data_by_pandas(
                data, 
                "t_cashflow_statement_dfcf",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "SECURITY_CODE": VARCHAR(16),
                    "DATE": VARCHAR(32)
                },
                single=True                
                )
            idx += 1
        except:
            print(v, idx)
            continue
    if init:
        db.execute("alter table t_cashflow_statement_dfcf add PRIMARY KEY(`SECURITY_NAME`, `DATE`)")


def store_stock_holder(
    date = [None],
    init=False
):
    idx = 0
    for v in date:
        try:
            data = stock_holder_num(v)
            print(idx, v)
            time.sleep(0.5)
            db.insert_data_by_pandas(
                data, 
                "t_stock_holder_num",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "SECURITY_CODE": VARCHAR(16),
                    "DATE": VARCHAR(32)
                },
                single=True                
                )
            idx += 1
        except:
            print(v, idx)
            continue
    if init:
        db.execute("alter table t_stock_holder_num add PRIMARY KEY(`SECURITY_CODE`, `DATE`)")

def store_forcast_report(
    date = [None],
    init=False
):
    idx = 0
    for v in date:
        try:
            data = forcast_report(v)
            print(idx, v)
            time.sleep(0.5)
            db.insert_data_by_pandas(
                data, 
                "t_stock_forcast_report",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "SECURITY_CODE": VARCHAR(16),
                    "PREDICT_FINANCE_CODE": VARCHAR(8)
                }
                #single=True                
                )
            idx += 1
        except Exception as e:
            print(v, idx, e)
            continue
    if init:
        db.execute("alter table t_stock_forcast_report add PRIMARY KEY(`SECURITY_CODE`, `PREDICT_FINANCE_CODE`)")

def store_eps_forecast(
    init=False
):
    try:
        data = eps_forecast()
        db.insert_data_by_pandas(
            data, 
            "t_stock_eps_forecast",
            {
                "SECURITY_NAME": VARCHAR(16),
                "SECURITY_CODE": VARCHAR(16)
            }
            #single=True                
            )
    except:
        print("error")
    if init:
        db.execute("alter table t_stock_eps_forecast add PRIMARY KEY(`SECURITY_CODE`)")

def store_stock_divide(
    latest=True,
    init=False
):
    idx = 0
    for k, v in stock_code.items():
        try:
            data = stock_divide(v)
            print(idx, k, v)
            time.sleep(0.5)
            #data["name"] = k
            #data["code"] = v
            db.insert_data_by_pandas(
                data, 
                "t_stock_divide",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "DATE": VARCHAR(32),
                },
                #single=True                
                )
            idx += 1
        except:
            print(k, v, idx)
            continue
    if init:
        db.execute("alter table t_stock_divide add PRIMARY KEY(`SECURITY_NAME`,`DATE`)")

def store_money_flow(
    latest=True,
    init=False
):
    idx = 0
    for k, v in stock_code.items():
        try:
            data = daily_money_flow(v)
            print(idx, k, v)
            time.sleep(0.5)
            data["SECURITY_NAME"] = k
            #data["code"] = v
            db.insert_data_by_pandas(
                data, 
                "t_stock_money_flow",
                {
                    "SECURITY_NAME": VARCHAR(16),
                    "DATE": VARCHAR(32),
                },
                #single=True                
                )
            idx += 1
        except:
            print(k, v, idx)
            continue
    if init:
        db.execute("alter table t_stock_money_flow add PRIMARY KEY(`SECURITY_NAME`, `DATE`)")

if __name__== "__main__":
    print("build financial")
    #store_money_flow()
    #alter table t_stock_money_flow add PRIMARY KEY(`SECURITY_NAME`, `DATE`);

    #store_main_business()
    #alter table t_main_business_f10 add PRIMARY KEY(`SECURITY_NAME`, `DATE`, `DIRECTION`, `CATEGORY`);

    #store_stock_holder(["2022-09-30", "2022-12-31", "2023-03-31", None])
    #alter table t_stock_holder_num add PRIMARY KEY(`SECURITY_CODE`, `DATE`);

    #store_cash_flow(["2022-09-30", "2022-12-31", "2023-03-31", None])
    #alter table t_cashflow_statement_dfcf add PRIMARY KEY(`SECURITY_NAME`, `DATE`);

    #store_financial_report_statement(latest=False)
    #alter table t_financial_report_statement add PRIMARY KEY(`SECURITY_NAME`, `DATE`);

    #store_income_profit(latest=False)
    #alter table t_income_profit_statement add PRIMARY KEY(`SECURITY_NAME`, `DATE`);

    #store_balance_sheet(latest=False)
    #alter table t_balance_sheet_statement add PRIMARY KEY(`SECURITY_NAME`, `DATE`);

    #store_forcast_report(["2022-09-30", "2022-12-31", "2023-03-31", None])
    #alter table t_stock_forcast_report add PRIMARY KEY(`SECURITY_CODE`, `PREDICT_FINANCE_CODE`);

    #store_eps_forecast()
    #alter table t_stock_eps_forecast add PRIMARY KEY(`SECURITY_CODE`);

    #store_stock_divide(latest=False)
    #alter table t_stock_divide add PRIMARY KEY(`SECURITY_NAME`,`DATE`);

    ###store_indictor()
    ####alter table t_main_business_f10 add PRIMARY KEY(`name`, `reporting_period`, `classification`, `classification_direction`);