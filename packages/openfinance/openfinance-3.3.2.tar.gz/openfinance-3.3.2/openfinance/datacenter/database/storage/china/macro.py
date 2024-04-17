# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:12:06 2022
author: zhubin_n@outlook.com
"""

import pandas as pd
import requests
from tqdm import tqdm
import json

from openfinance.datacenter.database.source.eastmoney.util import (
    trans_num, 
    trans_date
)

url = "https://datacenter-web.eastmoney.com/api/data/v1/get"

headers = {'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
}

def lpr(country="China"):
    """## chinese: 获取贷款基准利率lpr数据|lpr是多少
    ## english: Get lpr (Loan Prime Rate) data
    ## args: 
        country: "China"
    ## extra:
        http://data.eastmoney.com/cjsj/globalRateLPR.html
        LPR品种详细数据
    """
    sUrl = "http://datacenter.eastmoney.com/api/data/get"
    params = {
        "type": "RPTA_WEB_RATE",
        "sty": "ALL",
        "token": "894050c76af8597a853f5b408b759f5d",
        "p": "1",
        "ps": "2000",
        "st": "TRADE_DATE",
        "sr": "-1",
        "var": "WPuRCBoA",
        "rt": "52826782",
    }
    res = requests.get(sUrl, params=params)
    data_text = res.text
    data_json = json.loads(data_text.strip("var WPuRCBoA=")[:-1])
    df = pd.DataFrame(data_json["result"]["data"])
    df["LPR1Y"] = pd.to_numeric(df["LPR1Y"])
    df["LPR5Y"] = pd.to_numeric(df["LPR5Y"])
    df["RATE_1"] = pd.to_numeric(df["RATE_1"])
    df["RATE_2"] = pd.to_numeric(df["RATE_2"])
    df.sort_values(["TRADE_DATE"], inplace=True)
    df.reset_index(inplace=True, drop=True)
    df=df.rename(columns={"TRADE_DATE":"TIME"})
    df["TIME"] = df["TIME"].apply(lambda x: x[:10])
    return df

def money_supply(country="China"):
    """## chinese: 获取货币供应量|货币发行规模怎么样
    ## english: Get money supply or m0, m1, m2
    ## args: 
        country: 
    ## extra: 
        http://data.eastmoney.com/cjsj/hbgyl.html
    """
    params = {
        "columns" : "TIME,BASIC_CURRENCY,BASIC_CURRENCY_SAME,BASIC_CURRENCY_SEQUENTIAL,CURRENCY," + 
                    "CURRENCY_SAME,CURRENCY_SEQUENTIAL,FREE_CASH,FREE_CASH_SAME,FREE_CASH_SEQUENTIAL",
        "pageNumber" : "1",
        "pageSize": "12", 
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPT_ECONOMY_CURRENCY_SUPPLY",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1671530287536"
    }

    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)

    #total_page = data_json['result']['pages']
    total_page = 5
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber" : page,
                "p": page,
                "pageNo": page,
                "pageNum": page
            }
        )
        r = requests.get(url=url, params=params)
        data_json = json.loads(r.text)
        #print(data_json)
        temp_df = pd.DataFrame(data_json["result"]["data"])
        #new_cols=['日期','基础货币','基础货币同比','基础货币环比','活期存款','活期存款同比','活期存款环比','现金流','现金流同比','现金流环比']
        #temp_df=temp_df.rename(columns=dict(zip(temp_df.columns, new_cols)))        
        df = pd.concat([df, temp_df], ignore_index=True)
    df["TIME"] = df["TIME"].apply(lambda x: trans_date(x))
    return df

def cpi(country="China"):
    """## chinese: 获取消费者物价指数CPI|CPI是多少
    ## english: Get customer price index, cpi
    ## args: 
        country: 
    ## extra:  
        http://data.eastmoney.com/cjsj/cpi.html
    """
    params = {
        "columns" : "TIME,NATIONAL_SAME,NATIONAL_BASE,NATIONAL_SEQUENTIAL,NATIONAL_ACCUMULATE",
        "pageNumber" : "1",
        "pageSize": "12", 
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPT_ECONOMY_CPI",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1671530287536"
    }

    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)

    total_page = data_json['result']['pages']
    total_page = 5
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber" : page,
                "p": page,
                "pageNo": page,
                "pageNum": page
            }
        )
        r = requests.get(url=url, params=params)
        data_json = json.loads(r.text)
        temp_df = pd.DataFrame(data_json["result"]["data"])
        #new_cols=['日期','CPI同比','CPI环比','CPI累计']
        #temp_df=temp_df.rename(columns=dict(zip(temp_df.columns, new_cols)))
        df = pd.concat([df, temp_df], ignore_index=True)
    df["TIME"] = df["TIME"].apply(lambda x: trans_date(x))        
    return df


def gdp(country="China"):
    """## chinese: 获取国内生产总值GDP数据|GDP是多少
    ## english: Get the GDP, gross domestic product
    ## args: 
        country: 
    ## extra:
    """
    params = {
        "columns" : 
            "TIME,DOMESTICL_PRODUCT_BASE,FIRST_PRODUCT_BASE,SECOND_PRODUCT_BASE,THIRD_PRODUCT_BASE," +
            "SUM_SAME,FIRST_SAME,SECOND_SAME,THIRD_SAME",
        "pageNumber" : "1",
        "pageSize": "12", 
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPT_ECONOMY_GDP",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1671530287536"
    }

    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)

    #total_page = data_json['result']['pages']
    total_page = 5
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber" : page,
                "p": page,
                "pageNo": page,
                "pageNum": page
            }
        )
        r = requests.get(url=url, params=params)
        data_json = json.loads(r.text.replace("第1-", "第"))
        temp_df = pd.DataFrame(data_json["result"]["data"])
        #new_cols=['日期','国内生产总值','第一产业总值','第二产业总值','第三产业总值','国内生产总值同比','第一产业同比','第二产业同比','第三产业同比']
        #temp_df=temp_df.rename(columns=dict(zip(temp_df.columns, new_cols)))            
        df = pd.concat([df, temp_df], ignore_index=True)
    df["TIME"] = df["TIME"].apply(lambda x: trans_date(x))        
    return df


def international_trade():
    #url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "columns": "REPORT_DATE,EXIT_BASE,IMPORT_BASE,EXIT_BASE_SAME,IMPORT_BASE_SAME,EXIT_BASE_SEQUENTIAL,IMPORT_BASE_SEQUENTIAL",
        "pageNumber": 1,
        "pageSize": 20,
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1",
        "source": "WEB",
        "client": "WEB",
        "reportName": "RPT_ECONOMY_CUSTOMS",
        "_": "1702540624038"
    }
    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)
    df = pd.DataFrame(data_json["result"]["data"])
    cols = {
        "EXIT_BASE": "EXPORT_BASE",
        "IMPORT_BASE": "IMPORT_BASE",
        "EXIT_BASE_SAME": "EXPORT_BASE_YoY",
        "IMPORT_BASE_SAME": "IMPORT_BASE_YoY",
        "EXIT_BASE_SEQUENTIAL": "EXPORT_BASE_SEQUENTIAL",
        "IMPORT_BASE_SEQUENTIAL" : "IMPORT_BASE_SEQUENTIAL",
        "REPORT_DATE": "TIME"
    }
    df = df[list(cols.keys())].rename(columns=cols)
    df["TIME"] = df["TIME"].apply(lambda x: x[:10])
    return df    

def ppi(country="China"):
    """## chinese: 获取采购生产者物价指数PPI|PPI是多少
    ## english: Get Producer Price Index PPI
    ## args: 
        country: 
    ## extra:
    """
    params = {
        "columns" : "TIME,BASE,BASE_SAME,BASE_ACCUMULATE",
        "pageNumber" : "1",
        "pageSize": "12", 
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPT_ECONOMY_PPI",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1671530287536"
    }

    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)

    #total_page = data_json['result']['pages']
    total_page = 5
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber" : page,
                "p": page,
                "pageNo": page,
                "pageNum": page
            }
        )
        r = requests.get(url=url, params=params)
        data_json = json.loads(r.text)
        temp_df = pd.DataFrame(data_json["result"]["data"])
        #new_cols=['日期','生产者物价指数','同比','累计']
        #temp_df=temp_df.rename(columns=dict(zip(temp_df.columns, new_cols)))            
        df = pd.concat([df, temp_df], ignore_index=True)
    df["TIME"] = df["TIME"].apply(lambda x: trans_date(x))
    return df

# not right to fix later
def us_loan_rate(country="US"):
    """## chinese: 获取美联储贷款利率
    ## english: Get FED's rate
    ## args: 
        country: 
    ## extra:
    """
    params = {
        "columns" : "ALL",
        "pageNumber" : "1",
        "pageSize": "12", 
        #"sortColumns": "REPORT_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPT_STOCK_HEADERCHANGE",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1671530287536"
    }

    data = requests.get(url + "&filter=(SECURITY_CODE%3D%22601138%22)", headers=headers, params=params)
    data_json = json.loads(data.text)

    #total_page = data_json['result']['pages']
    total_page = 5
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber" : page,
                "p": page,
                "pageNo": page,
                "pageNum": page
            }
        )
        r = requests.get(url=url, params=params)
        data_json = json.loads(r.text)
        print(data_json)
        temp_df = pd.DataFrame(data_json["result"]["data"])
        #new_cols=['发布日期','前值','公布值']
        #temp_df=temp_df.rename(columns=dict(zip(temp_df.columns, new_cols)))            
        df = pd.concat([df, temp_df], ignore_index=True)
    df["TIME"] = df["TIME"].apply(lambda x: trans_date(x))
    return df


def consumer_faith(country="China"):
    """## chinese: 获取消费者信息指数
    ## english: Get consumer faith index
    ## args: 
        country: 
    ## extra:
    """
    params = {
        "columns" : "TIME,CONSUMERS_FAITH_INDEX,FAITH_INDEX_SAME,FAITH_INDEX_SEQUENTIAL",
        "pageNumber" : "1",
        "pageSize": "12", 
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPT_ECONOMY_FAITH_INDEX",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1671530287536"
    }

    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)

    #total_page = data_json['result']['pages']
    total_page = 5
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber" : page,
                "p": page,
                "pageNo": page,
                "pageNum": page
            }
        )
        r = requests.get(url=url, params=params)
        data_json = json.loads(r.text)
        temp_df = pd.DataFrame(data_json["result"]["data"])
        #new_cols=['日期','消费者信心指数','同比','环比']
        #temp_df=temp_df.rename(columns=dict(zip(temp_df.columns, new_cols)))            
        df = pd.concat([df, temp_df], ignore_index=True)
    df["TIME"] = df["TIME"].apply(lambda x: trans_date(x))
    return df


def pmi(country="China"):
    """## chinese: 获取采购经理人指数PMI|PMI是多少
    ## english: Get Purchasing Managers Index, PMI 
    ## args: 
        country: 
    ## extra:
    """
    params = {
        "columns" : "TIME,MAKE_INDEX,MAKE_SAME,NMAKE_INDEX,NMAKE_SAME",
        "pageNumber" : "1",
        "pageSize": "12", 
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPT_ECONOMY_PMI",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1671530287536"
    }

    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)
    #total_page = data_json['result']['pages']
    total_page = 5
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber" : page,
                "p": page,
                "pageNo": page,
                "pageNum": page
            }
        )
        r = requests.get(url=url, params=params)
        data_json = json.loads(r.text)
        #print(data_json)
        temp_df = pd.DataFrame(data_json["result"]["data"])
        #new_cols=['日期','制造业指数','制造业同比','非制造业指数','非制造业同比']
        #temp_df=temp_df.rename(columns=dict(zip(temp_df.columns, new_cols)))           
        df = pd.concat([df, temp_df], ignore_index=True)
    df["TIME"] = df["TIME"].apply(lambda x: trans_date(x))        
    return df

def treasury_bond_yield():
    # https://data.eastmoney.com/cjsj/zmgzsyl.html
    params = {
        "columns" : "ALL",
        "pageNumber" : "1",
        "pageSize": "500", 
        "sortColumns": "SOLAR_DATE",
        "sortTypes": "-1", 
        "source": "WEB", 
        "client":"WEB",
        "reportName": "RPTA_WEB_TREASURYYIELD",
        "token": "894050c76af8597a853f5b408b759f5d",
        "pageNo": "1",
        "pageNum": "1",
        "_" : "1692943820524"
    }

    data = requests.get(url, headers=headers, params=params)
    data_json = json.loads(data.text)
    df = pd.DataFrame(data_json["result"]["data"])

    cols = {
        "SOLAR_DATE": "DATE",
        "EMM00588704": "CNY2Y",
        "EMM00166466": "CNY10Y",
        "EMG00001306": "US2Y",
        "EMG00001310": "US10Y",
        "EMG01339436": "US10Y_2Y"
    }
    df = df[list(cols.keys())].rename(columns=cols)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    return df

##############################################################################
######################## Not for Analysis ####################################
##############################################################################

###同业拆借利率
def interbank_rate(market='sh'):
    """## chinese: 获取银行市场拆借利率|市场拆解利率是多少
    ## english: Get the shibor, interbank offered rate
    ## args: 
        market: [sh, ch, hk]
    ##
    """
    market='sh'
    fc = None
    if fc is None:
        fc='USD'
    if market=='ch':
        fc='CNY'
        period=['隔夜','1周','2周','3周','1月','2月','3月','4月','6月','9月','1年']
    elif market=='eu':
        fc='EUR'
        period=['1周','2周','3周','1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','1年']
    elif market=='l':
        period=['隔夜','1周','1月','2月','3月','8月']
    elif market=='hk':
        period=['隔夜','1周','2周','1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月''1年']
    elif market=='s':
        period=['1月','2月','3月','6月','9月','1年']
    else:
        fc='CNY'
        #period=['隔夜','1周','2周','1月','3月','6月','9月','1年']
        period = ['隔夜','1周','1月','6月','1年']


    df=interbank_rate_full(market, fc, period[0])[['报告日','利率']]
    df=df.rename(columns={'利率':period[0]})
    for p in period[1:]:
        try:
            temp=interbank_rate(market, fc, p)[['报告日','利率']]
            temp=temp.rename(columns={'利率':p})
            df=pd.merge(df,temp,how='outer')
        except:
            continue
    df= df.sort_values('报告日')
    df.reset_index(inplace=True, drop=True)
    return df

def interbank_rate_full(market, fc, indicator):
    '''market:同业拆借市场简称，各个市场英文缩写为：
    {'sh':'上海银行同业拆借市场','ch':'中国银行同业拆借市场','l':'伦敦银行同业拆借市场',
     'eu':'欧洲银行同业拆借市场','hk':'香港银行同业拆借市场','s':'新加坡银行同业拆借市场'}
    香港市场，fc可选：'港元'，'美元','人民币'；新加坡市场，fc可选：'星元','美元';
    伦敦市场，fc可选：'英镑','美元','欧元','日元';
    '''
    market_dict = {
        "上海银行同业拆借市场": "001",
        "中国银行同业拆借市场": "002",
        "伦敦银行同业拆借市场": "003",
        "欧洲银行同业拆借市场": "004",
        "香港银行同业拆借市场": "005",
        "新加坡银行同业拆借市场": "006",
        "sh": "001",
        "ch": "002",
        "l": "003",
        "eu": "004",
        "hk": "005",
        "s": "006",
    }
    fc_dict = {
        "人民币": "CNY",
        "英镑": "GBP",
        "欧元": "EUR",
        "美元": "USD",
        "港币": "HKD",
        "港元": "HKD",
        "星元": "SGD",
        "新元": "SGD",
    }
    
    if fc.isalpha():
        fc=fc.upper()
    else:
        fc=fc_dict[fc]
    if market.isalpha():
        market=market.lower()
    market=market_dict[market]
    
    if market=="005" and fc=="CNY":
        fc="CNH"
    
    indicator_dict = {
        "隔夜": "001",
        "1周": "101",
        "2周": "102",
        "3周": "103",
        "1月": "201",
        "2月": "202",
        "3月": "203",
        "4月": "204",
        "5月": "205",
        "6月": "206",
        "7月": "207",
        "8月": "208",
        "9月": "209",
        "10月": "210",
        "11月": "211",
        "1年": "301",
    }

    params = {
        "reportName": "RPT_IMP_INTRESTRATEN",
        "columns": "REPORT_DATE,REPORT_PERIOD,IR_RATE,CHANGE_RATE,INDICATOR_ID,LATEST_RECORD,MARKET,MARKET_CODE,CURRENCY,CURRENCY_CODE",
        "quoteColumns": "",
        "filter": f"""(MARKET_CODE="{market}")(CURRENCY_CODE="{fc}")(INDICATOR_ID="{indicator_dict[indicator]}")""",
        "pageNumber": "1",
        "pageSize": "100",
        "sortTypes": "-1",
        "sortColumns": "REPORT_DATE",
        "source": "WEB",
        "client": "WEB",
        "p": "1",
        "pageNo": "1",
        "pageNum": "1",
        "_": "1653376974939",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    #total_page = data_json["result"]["pages"]
    df = pd.DataFrame()
    total_page = 2
    for page in tqdm(range(1, total_page + 1), leave=False):
        params.update(
            {
                "pageNumber": page,
                "p": page,
                "pageNo": page,
                "pageNum": page,
            }
        )
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)
    df.columns = [
        "报告日",
        "-",
        "利率",
        "涨跌",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
    ]
    df = df[
        [
            "报告日",
            "利率",
            "涨跌",
        ]
    ]
    df["报告日"] = pd.to_datetime(df["报告日"]).dt.date
    df["利率"] = pd.to_numeric(df["利率"])
    df["涨跌"] = pd.to_numeric(df["涨跌"])
    df.sort_values(["报告日"], inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df




def macro_data(flag=None):
    """## chinese: 获取国家宏观经济数据|国家宏观经济怎么样
    ## english: Get macro economic data
    ## args: 
        flag: lpr:贷款基准利率 ms:货币供应量 cpi:消费者物价指数 ppi:工业品出厂价格指数 pmi:采购经理人指数, 默认 gdp
    ##
    """
    if flag=='lpr':
        return lpr()
    elif flag=='ms':
        return money_supply()
    elif flag=='cpi':
        return cpi()
    elif flag=='ppi':
        return ppi()
    elif flag=='pmi':
        return pmi()
    else:
        return gdp()
