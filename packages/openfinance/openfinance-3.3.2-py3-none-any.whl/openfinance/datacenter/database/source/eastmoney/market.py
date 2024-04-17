
import requests
import json
import pandas as pd

from tqdm import tqdm
from openfinance.datacenter.database import EMPTY_DATA

def market_data(country="China"):
    """## chinese: 获取市场成交情况|大盘成交数据
    ## english: Get Market Condition
    ## args: 
        country: "China"
    ## extra:
        http://quote.eastmoney.com/newapi/sczm
    """
    sUrl = "http://quote.eastmoney.com/newapi/sczm"
    data_json = requests.get(sUrl).json()
    #print(data_json)
    total_money = data_json['ss']['tv'] + data_json['cyb']['tv']  + data_json['hs']['tv']
    return str(round(total_money/10000, 2)) + "万亿元"


def market_loan_money_single(code=""):
    """## chinese: 获取融资占比|融资情况
    ## english: Get daily loan money
    ## args: 
        country: "China"
    ## extra:
        http://datacenter-web.eastmoney.com/api/data/get?callback=jQuery35105423936054919123_1689063750558&type=RPT_MARGIN_MARGINPROFILE&sty=TRADE_DATE%2CMARKET%2CBOARD_CODE%2CFIN_BALANCE%2CLOAN_BALANCE%2CMARGIN_BALANCE%2CFIN_BUY_AMT&extraCols=&filter=&p=1&ps=5&sr=&st=&token=&var=&source=QuoteWeb&client=WEB&_=1689063750559
    """    
    sUrl = "http://datacenter-web.eastmoney.com/api/data/get"
    params = {
        "type": "RPT_MARGIN_MARGINPROFILE",
        "sty": "TRADE_DATE,MARKET,BOARD_CODE,FIN_BALANCE,LOAN_BALANCE,MARGIN_BALANCE,FIN_BUY_AMT",
        "extraCols": "",
        "filter": "",
        "ps": "5",
        "st": "",
        "sr": "",
        "token": "",
        "var": "",
        "source": "QuoteWeb",
        "client": "WEB",
        "_": 1689063750559
    }
    res = requests.get(sUrl, params=params)
    data_text = json.loads(res.text)
    for data in data_text['result']['data']:
        print(data)
        if data['MARKET'] == "两市":
            return str(round(data['FIN_BUY_AMT']/100000000, 1)) + "亿元"
    return EMPTY_DATA


def north_money_flow(flag= "北上"):
    """## chinese: 获取外资流入情况|外资流入情况
    ## english: Get foreign money
    ## args: 
        flag: {"沪股通", "深股通", "北上"}
    ## extra:  
        http://data.eastmoney.com/hsgtcg/
    """
    url = "http://push2his.eastmoney.com/api/qt/kamt.kline/get"
    params = {
        "fields1": "f1,f3,f5",
        "fields2": "f51,f52",
        "klt": "101",
        "lmt": "300",
        "ut": "b2884a393a59ad64002292a3e90d46a5",
        "cb": "jQuery18305732402561585701_1584961751919",
        "_": "1584962164273",
    }
    r = requests.get(url, params=params)
    data_text = r.text
    data_json = json.loads(data_text[data_text.find("{") : -2])
    result = {
        "DATE": [],
        "VOLUME": []
    }
    for i in data_json['data']['s2n']:
        d = i.split(",")
        result['DATE'].append(d[0])
        result['VOLUME'].append(d[1])
    return result
