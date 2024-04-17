# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:24:19 2022
"""

import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from py_mini_racer import py_mini_racer
from tqdm import tqdm
from jsonpath import jsonpath

from openfinance.datacenter.database import EMPTY_DATA
from openfinance.datacenter.database.source.eastmoney.util import (
    trans_num,
    get_code_id,
    session,
    request_header
)

def north_money_stock(n=1):
    """
    获取东方财富北向资金增减持个股情况
    http://data.eastmoney.com/hsgtcg/list.html
    n:  代表n日排名，n可选1、3、5、10、‘M’，‘Q','Y'
    即 {'1':"今日", '3':"3日",'5':"5日", '10':"10日",'M':"月", 'Q':"季", 'Y':"年"}
    """
    url = "http://data.eastmoney.com/hsgtcg/list.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    date = (
        soup.find("div", attrs={"class": "title"})
        .find("span")
        .text.strip("（")
        .strip("）"))
    url = "http://datacenter-web.eastmoney.com/api/data/v1/get"
    
    _type=str(n).upper()
    type_dict={'1':"今日", '3':"3日",'5':"5日", '10':"10日",'M':"月", 'Q':"季", 'Y':"年"}
    period=type_dict[_type]
    filter_str = (f"""(TRADE_DATE='{date}')(INTERVAL_TYPE="{_type}")""")
    params = {
        "sortColumns": "ADD_MARKET_CAP",
        "sortTypes": "-1",
        "pageSize": "50000",
        "pageNumber": "1",
        "reportName": "RPT_MUTUAL_STOCK_NORTHSTA",
        "columns": "ALL",
        "source": "WEB",
        "client": "WEB",
        "filter": filter_str,
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    page_num = data_json["result"]["pages"]
    df = pd.DataFrame()
    for page in tqdm(range(1, page_num + 1), leave=False):
        params.update({"pageNumber": page})
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.reset_index(inplace=True)
    df["index"] = range(1, len(df) + 1)
    df.columns = [
        "序号","_","_","日期","_","名称","_","_","代码","_", "_","_","_",
        "持股数","持股市值","持股占流通股比","持股占总股本比",
        "收盘","涨幅","_","所属板块","_","_","_","_","_","_","_", "_",
        "_","_", f'{period}增持市值',f'{period}增持股数',f'{period}增持市值增幅',
        f'{period}增持占流通股比',f'{period}增持占总股本比',
        "_","_","_","_","_","_","_",]
    df = df[
        ["代码","名称","收盘","涨幅", "持股数","持股市值","持股占流通股比",
         "持股占总股本比",f'{period}增持股数',f'{period}增持市值',
         f'{period}增持市值增幅',f'{period}增持占流通股比',f'{period}增持占总股本比',
        "所属板块", "日期",] ]
    df["日期"] = pd.to_datetime(df["日期"]).dt.date
    ignore_cols = ["代码","名称","所属板块", "日期",]
    df = trans_num(df, ignore_cols)
    return df
