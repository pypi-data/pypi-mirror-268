"""
Created on Fri Sep 30 13:53:48 2022

"""
import time
import json
import requests
import calendar
import pandas as pd
from datetime import datetime
from jsonpath import jsonpath
from tqdm import tqdm
from bs4 import BeautifulSoup

from openfinance.datacenter.database.source.eastmoney.trade import (
    market_realtime
)
from openfinance.datacenter.database.source.eastmoney.util import (
    latest_report_date,    
    trans_num,
    get_code_id,
    request_header, 
    session,
    trans_date
)

def financial_statement(name = "AAPL"):
    """
    获取东方财富年报季度现金流表
    https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=AAPL&type=web&color=w#/cwfx/xjllb
    https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_USF10_FN_GMAININDICATOR&columns=USF10_FN_GMAININDICATOR&quoteColumns=&filter=(SECUCODE%3D%22PG.N%22)&pageNumber=1&pageSize=6&sortTypes=-1&sortColumns=REPORT_DATE&source=SECURITIES&client=PC&v=008607020948791444
    name: 如"AAPL"
    """
    url = "https://datacenter.eastmoney.com/securities/api/data/v1/get"
    params = {
        "reportName": "RPT_USF10_FN_GMAININDICATOR",
        "columns": "USF10_FN_GMAININDICATOR",
        # columns: "ORG_CODE,SECURITY_CODE,SECUCODE,SECURITY_NAME_ABBR,STD_REPORT_DATE,REPORT_DATE,DATE_TYPE,REPORT_TYPE,REPORT_DATA_TYPE,ACCOUNT_STANDARD,ACCOUNT_STANDARD_NAME,CURRENCY,CURRENCY_NAME,ORGTYPE,TOTAL_INCOME,TOTAL_INCOME_YOY,PREMIUM_INCOME,PREMIUM_INCOME_YOY,PARENT_HOLDER_NETPROFIT,PARENT_HOLDER_NETPROFIT_YOY,BASIC_EPS_CS,BASIC_EPS_CS_YOY,DILUTED_EPS_CS,PAYOUT_RATIO,CAPITIAL_RATIO,ROE,ROE_YOY,ROA,ROA_YOY,DEBT_RATIO,DEBT_RATIO_YOY,EQUITY_RATIO"
        "quoteColumns": "",
        "filter": f'(SECUCODE="{name.replace(".", "_")}.N")',
        "pageNumber": 1,
        "pageSize": 6,
        "sortTypes": -1,
        "sortColumns": "REPORT_DATE",
        "source": "SECURITIES",
        "client": "PC",
        "v": "008607020948791444",
    }
    try:
        res = requests.get(url, params=params)
        #print(res.content)
        data_json = res.json()
        #print(data_json)
        data = data_json["result"]["data"]
    except:
        params['filter'] = f'(SECUCODE="{name.replace(".", "_")}.O")'  # NASDAQ
        res = requests.get(url, params=params)
        #print(res.content)
        data_json = res.json()
        #print(data_json)
        data = data_json["result"]["data"]        
    cols = [
        "SECURITY_CODE",
        "SECURITY_NAME_ABBR",
        "STD_REPORT_DATE",
        "DATE_TYPE",
        "OPERATE_INCOME_YOY",
        "GROSS_PROFIT_YOY",
        "PARENT_HOLDER_NETPROFIT_YOY",
        "DILUTED_EPS",
        "GROSS_PROFIT_RATIO",
        "NET_PROFIT_RATIO",
        "ACCOUNTS_RECE_TR",
        'INVENTORY_TDAYS',
        'TOTAL_ASSETS_TDAYS',
        'ROE_AVG',
        'ROA',
        'CURRENT_RATIO',
        'SPEED_RATIO',
        'OCF_LIQDEBT',
        'DEBT_ASSET_RATIO',
        'EQUITY_RATIO',
        'BASIC_EPS_YOY',
        'GROSS_PROFIT_RATIO_YOY',
        'NET_PROFIT_RATIO_YOY',
        'ROE_AVG_YOY',
        'ROA_YOY',
        'DEBT_ASSET_RATIO_YOY',
        'CURRENT_RATIO_YOY',
        'SPEED_RATIO_YOY'   
    ]

    df = pd.DataFrame(data)[cols].rename(columns={
        "SECURITY_NAME_ABBR": "SECURITY_NAME",
        "STD_REPORT_DATE": "DATE"
        })
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])    
    return df

def cashflow_statement(name = "AAPL"):
    """
    获取东方财富年报季度现金流表
    https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=AAPL&type=web&color=w#/cwfx/xjllb
    name: 如"AAPL"
    """
    url = "https://datacenter.eastmoney.com/securities/api/data/v1/get"
    params = {  
        "reportName": "RPT_USSK_FN_CASHFLOW",  
        "columns": "SECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,REPORT,REPORT_DATE,STD_ITEM_CODE,AMOUNT",  
        "quoteColumns": "",  
        "filter": f"(SECURITY_CODE='{name}')(REPORT in ('2023Q1','2022Q4','2022Q3','2022Q2','2022Q1','2021Q4'))",  
        "pageNumber": "",  
        "pageSize": "",  
        "sortTypes": "1,-1",  
        "sortColumns": "STD_ITEM_CODE,REPORT_DATE",  
        "source": "SECURITIES",  
        "client": "PC",  
        "v": "024181877411384534"  
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    return data_json

def balance_sheet_statement(name = "AAPL"):
    """
    获取东方财富年报季度现金流表
    https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=AAPL&type=web&color=w#/cwfx/xjllb
    name: 如"AAPL"
    """
    url = "https://datacenter.eastmoney.com/securities/api/data/v1/get"  
    params = {  
        'reportName': 'RPT_USF10_FN_BALANCE',  
        'columns': 'SECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,REPORT_DATE,REPORT_TYPE,REPORT,STD_ITEM_CODE,AMOUNT',  
        'quoteColumns': '',  
        'filter': f'(SECURITY_CODE="{name}")(REPORT in ("2023/Q1","2022/Q1","2021/Q1","2020/Q1","2019/Q1","2018/Q1"))',  
        'pageNumber': '',  
        'pageSize': '',  
        'sortTypes': '1,-1',  
        'sortColumns': 'STD_ITEM_CODE,REPORT_DATE',  
        'source': 'SECURITIES',  
        'client': 'PC',  
        'v': '037967688588902204'  
    }    
    res = requests.get(url, params=params)
    data_json = res.json()
    return data_json

def operation_statement(name = "AAPL"):
    """
    获取东方财富年报季度现金流表
    https://emweb.eastmoney.com/PC_USF10/pages/index.html?code=AAPL&type=web&color=w#/cwfx/xjllb
    name: 如"AAPL"
    """
    url = "https://datacenter.eastmoney.com/securities/api/data/v1/get"  

    {  
        "reportName": "RPT_USF10_FN_INCOME",  
        "columns": "SECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,REPORT,REPORT_DATE,STD_ITEM_CODE,AMOUNT",  
        "quoteColumns": "",  
        "filter": f"(SECUCODE='{name}.O')(REPORT in ('2023/Q1','2022/Q4','2022/Q3','2022/Q2','2022/Q1','2021/Q4'))",  
        "pageNumber": "",  
        "pageSize": "",  
        "sortTypes": "1,-1",  
        "sortColumns": "STD_ITEM_CODE,REPORT_DATE",  
        "source": "SECURITIES",  
        "client": "PC",  
        "v": "08405948136984875"  
    }     
    res = requests.get(url, params=params)
    data_json = res.json()
    return data_json


def get_all_stock(total_num=800):
    """
        total_num: rank by volume
    """
    page = int(total_num/60)
    headers = {
        "authority": "stock.finance.sina.com.cn",
        "method": "GET",
        "path": "/usstock/api/jsonp.php/IO.XSRV2.CallbackList['fa8Vo3U4TzVRdsLs']/US_CategoryService.getList?page=1&num=20&sort=&asc=0&market=&id=",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cache-control": "max-age=0",
        "cookie": "UOR=,finance.sina.com.cn,; ULV=1702970793403:1:1:1::; SINAGLOBAL=113.84.33.155_1702970793.647528; Apache=113.84.33.155_1702970793.647529",
        "sec-ch-ua": 'Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    }
    stocks = []
    for i in range(page):
        params = {
            "page": i+1,
            "num": 60,
            "sort": "",
            "asc": 0,
            "market": "",
            "id": ""
        }
        url = "https://stock.finance.sina.com.cn/usstock/api/jsonp.php/IO.XSRV2.CallbackList['fa8Vo3U4TzVRdsLs']/US_CategoryService.getList"
        response = requests.get(url, headers=headers, params=params)
        data = response.content[91:-2]
        data_json = json.loads(data)
        for d in data_json['data']:
            stocks.append((d['cname'], d['category'], d['symbol']))
    return stocks


# https://docs.data.nasdaq.com/docs/in-depth-usage# -*- coding: utf-8 -*-
# Nasdaq nasdaqdatalink.ApiConfig.api_key = "VFs_mgJE86wq4zTeyAJk"
# GET https://data.nasdaq.com/api/v3/datasets/{database_code}/{dataset_code}/data.{return_format}
# curl "https://data.nasdaq.com/api/v3/datasets/WIKI/FB/data.json?api_key=YOURAPIKEY"



