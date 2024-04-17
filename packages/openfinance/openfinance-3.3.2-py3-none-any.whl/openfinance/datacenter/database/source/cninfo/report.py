# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:53:48 2022

"""
import requests
import calendar
import time
import pandas as pd

from datetime import datetime
from jsonpath import jsonpath
from tqdm import tqdm
from bs4 import BeautifulSoup

from openfinance.datacenter.database.source.cninfo.util import cn_headers

def stock_holder_con():
    """获取实际控制人持股变动
    巨潮资讯-数据中心-专题统计-股东股本-实际控制人持股变动
    http://webapi.cninfo.com.cn/#/thematicStatistics
    """
    url = "http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1033"
    
    params = {"ctype": "",}
    r = requests.post(url, headers=cn_headers, params=params)
    data_json = r.json()
    df = pd.DataFrame(data_json["records"])
    old_cols=["控股比例","控股数量","简称","实控人",
        "直接控制人","控制类型","代码","变动日期",]
    
    new_cols=["变动日期","代码","简称","控股比例","控股数量","实控人",
        "直接控制人","控制类型"]
    df.columns = old_cols
    df = df[new_cols]
    df["变动日期"] = pd.to_datetime(df["变动日期"]).dt.date
    df[["控股数量","控股比例"]] =df[["控股数量","控股比例"]].apply(lambda s:pd.to_numeric(s))
    return df