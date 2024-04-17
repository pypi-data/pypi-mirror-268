import time
import requests
import json
import calendar
import pandas as pd
from datetime import datetime

from tqdm import tqdm
from bs4 import BeautifulSoup

from openfinance.datacenter.database.source.eastmoney.trade import (
    market_realtime
)
from openfinance.datacenter.database.source.eastmoney.util import (
    get_current_date,    
    trans_num,
    get_code_id,
    request_header, 
    session,
    trans_date
)

def north_money_to_sector(date=None):
    """
    获取东方财富北向资金行业增持情况
    """
    if date is None:
        date=get_current_date()
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"

    params = {
        "sortColumns": "ADD_MARKET_CAP",
        "sortTypes": "-1",
        "pageSize": "500",
        "pageNumber": 1,
        "reportName": "RPT_MUTUAL_BOARD_HOLDRANK_WEB",
        "columns": "ALL",
        "quoteColumns": "f3~05~SECURITY_CODE~INDEX_CHANGE_RATIO",
        "source": "WEB",
        "client": "WEB",
        "filter": f"""(TRADE_DATE='{date}')""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    pages = data_json["result"]["pages"]

    df = pd.DataFrame(data_json["result"]["data"])
    for i in range(2, pages+1, 1):
        params.update({"pageNumber": i})
        res = requests.get(url, params=params)
        data_json = res.json()
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)

    columns = {
        "BOARD_NAME": "INDUSTRY_NAME",
        "ADD_MARKET_CAP": "MARKET_CAPITAL_INCOME",
        "ADD_RATIO": "MARKET_CAPITAL_INCOME_RATIO",
        "INTERVAL_TYPE": "INTERVAL_TYPE",
        "TRADE_DATE": "DATE"
    }
    df = df[list(columns.keys())].rename(columns=columns)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    return df


def industy_all_valuation():
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "qgqp_b_id=164c76d2ed75802b814949a81b3b6191; websitepoptg_show_time=1703145371497; HAList=ty-1-601360-%u4E09%u516D%u96F6%2Cty-0-300949-%u5965%u96C5%u80A1%u4EFD%2Cty-106-BLK-%u8D1E%u83B1%u5FB7%2Cty-105-AAPL-%u82F9%u679C%2Cty-106-PG-%u5B9D%u6D01%2Cty-100-DJIA-%u9053%u743C%u65AF%2Cty-106-MS-%u6469%u6839%u58EB%u4E39%u5229%2Cty-106-BRK_A-%u4F2F%u514B%u5E0C%u5C14%u54C8%u6492%u97E6-A%2Cty-106-GME-%u6E38%u620F%u9A7F%u7AD9; st_si=93775926910693; st_asi=delete; st_pvi=54709136970065; st_sp=2023-12-19%2015%3A13%3A28; st_inirUrl=http%3A%2F%2Fquote.eastmoney.com%2Fcenter%2Fgridlist.html; st_sn=2; st_psi=20231226144155291-113300303065-2004315192; JSESSIONID=931248717DA1D240295441B47CD58FA4",
        "Host": "datacenter-web.eastmoney.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    params = {
        #"callback": "jQuery11230885902819389405_1703572892543",
        "sortColumns": "PE_TTM",
        "sortTypes": "1",
        "pageSize": "50",
        "pageNumber": 1,
        "reportName": "RPT_VALUEINDUSTRY_DET",
        "columns": "ALL",
        "quoteColumns": "",
        "source": "WEB",
        "client": "WEB",
        "filter": "(TRADE_DATE='2023-12-25')"
    }

    response = requests.get(url, params=params, headers=headers)
    jsondata = json.loads(response.text)
    df = pd.DataFrame(jsondata["result"]["data"])

    pages = jsondata["result"]["pages"]
    for i in range(pages-1):
        params["pageNumber"] = i + 2
        response = requests.get(url, params=params, headers=headers)
        jsondata = json.loads(response.text)
        temp_df = pd.DataFrame(jsondata["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)

    columns = {
        "BOARD_NAME": "INDUSTRY_NAME",
        "BOARD_CODE": "INDUSTRY_CODE",
        "PE_TTM": "PE_TTM",
        "PE_LAR": "PE_LAR",
        "PB_MRQ": "PB_MRQ",
        "PS_TTM":"PS_TTM",
        "PCF_OCF_TTM": "PCF_OCF_TTM",
        "PEG_CAR": "PEG",
        "TRADE_DATE": "DATE"
    }
    df = df[list(columns.keys())].rename(columns=columns)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    return df