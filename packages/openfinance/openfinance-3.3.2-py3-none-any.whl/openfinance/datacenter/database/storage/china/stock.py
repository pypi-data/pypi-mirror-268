# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:53:48 2022

"""
import time
import requests
import calendar
import pandas as pd
from datetime import datetime
from jsonpath import jsonpath
from tqdm import tqdm
from bs4 import BeautifulSoup

from openfinance.datacenter.database.source.eastmoney.trade import (
    market_realtime,
    stock_code_dict
)
from openfinance.datacenter.database.source.eastmoney.util import (
    latest_report_date,    
    trans_num,
    get_code_id,
    request_header, 
    session,
    trans_date
)

def income_statement(date = None):
    """
    获取东方财富年报季报-利润表
    http://data.eastmoney.com/bbsj/202003/lrb.html
    date: 如"2022-03-31", "2022-06-30"
    """
    date=trans_date(date)
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "NOTICE_DATE,SECURITY_CODE",
        "sortTypes": "-1,-1",
        "pageSize": "500",
        "pageNumber": "1",
        "reportName": "RPT_DMSK_FN_INCOME",
        "columns": "ALL",
        "filter": f"""(SECURITY_TYPE_CODE in ("058001001","058001008"))(TRADE_MARKET_CODE!="069001017")(REPORT_DATE='{date}')""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    page_num = data_json["result"]["pages"]
    df = pd.DataFrame()
    for page in tqdm(range(1, page_num + 1), leave=False):
        params.update(
            {
                "pageNumber": page,
            }
        )
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.reset_index(inplace=True)
    df["index"] = df.index + 1
    df.columns = ["序号","_","代码","_","_","简称","_","_","_","_","_","_",
        "_","公告日", "_","净利润","营业总收入","营业总支出","_","营业支出",
        "_","_","销售费用","管理费用","财务费用","营业利润","利润总额",
        "_","_","_", "_","_","_","_","_","_", "_","_","_","_","_","_",
        "营业总收入同比","_","净利润同比", "_","_",]
    
    df = df[["代码","简称","净利润","净利润同比","营业总收入","营业总收入同比",
            "营业支出","销售费用","管理费用","财务费用","营业总支出",
            "营业利润","利润总额","公告日",]]
    
    df["公告日"] = pd.to_datetime(df["公告日"]).dt.date
    cols = ['代码', '简称', '公告日',]
    df = trans_num(df, cols).round(2)
    return df

# RPT_DMSK_FN_BALANCE 资产负债表
def balance_sheet_statement(code= None, latest=False, page_num=8):
    """
    获取东方财富资产负债表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    date: 如"20220331", "20220630"
    """
    #print(code)
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    if latest:
        page_num = 1
    params = {
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1",
        "pageSize": str(page_num),
        "pageNumber": "1",
        "reportName": "RPT_DMSK_FN_BALANCE",
        "columns": "ALL",
        "filter": f"""(SECURITY_CODE={code})""",
    }
    df = pd.DataFrame()
    res = requests.get(url, params=params)
    data_json = res.json()
    #print(data_json)
    df = pd.DataFrame(data_json["result"]["data"])
    cols = {
        "SECURITY_CODE": "SECURITY_CODE",
        "SECURITY_NAME_ABBR": "SECURITY_NAME",
        "INDUSTRY_NAME": "INDUSTRY_NAME",
        "REPORT_DATE": "DATE",
        "TOTAL_ASSETS": "TOTAL_ASSETS",
        "FIXED_ASSET": "FIXED_ASSET",
        "MONETARYFUNDS": "MONETARY_FUNDS",
        "MONETARYFUNDS_RATIO": "YoY_MONETARY_FUNDS",
        "ACCOUNTS_RECE": "ACCOUNTS_RECEIVABLE",
        "ACCOUNTS_RECE_RATIO": "YoY_ACCOUNTS_RECEIVABLE",
        "INVENTORY": "INVENTORY",
        "INVENTORY_RATIO": "YoY_INVENTORY",
        "TOTAL_LIABILITIES": "TOTAL_LIABILITIES",
        "ACCOUNTS_PAYABLE": "ACCOUNTS_PAYABLE",
        "ACCOUNTS_PAYABLE_RATIO": "YoY_ACCOUNTS_PAYABLE",
        "ADVANCE_RECEIVABLES": "ADVANCE_RECEIVABLES",
        "ADVANCE_RECEIVABLES_RATIO": "YoY_ADVANCE_RECEIVABLES",
        "TOTAL_EQUITY": "TOTAL_EQUITY",
        "TOTAL_EQUITY_RATIO": "YoY_TOTAL_EQUITY",
        "TOTAL_ASSETS_RATIO": "YoY_TOTAL_ASSETS",
        "TOTAL_LIAB_RATIO": "YoY_TOTAL_LIAB",
        "CURRENT_RATIO": "YoY_CURRENT",
        "DEBT_ASSET_RATIO": "DEBT_ASSET_RATIO"
    }
    df=df[list(cols.keys())].rename(columns=cols)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    return df

def financial_report_statement(code= None, latest=False, page_num=8):
    """
    获取东方财富业绩报表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    """
    #print(code)
    if latest:
        page_num = 1
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "REPORTDATE",
        "sortTypes": "-1",
        "pageSize": str(page_num),
        "pageNumber": "1",
        "reportName": "RPT_LICO_FN_CPD",
        "columns": "ALL",
        "filter": f"""(SECURITY_CODE={code})""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    #print(data_json)

    df = pd.DataFrame(data_json["result"]["data"])

    cols = {
        'SECURITY_CODE': 'SECURITY_CODE', 
        'SECURITY_NAME_ABBR': 'SECURITY_NAME', 
        'TOTAL_OPERATE_INCOME': 'TOTAL_OPERATE_INCOME', 
        'YSTZ': 'YoY_REVENUE', 
        'YSHZ': 'SEQUENTIAL_REVENUE', 
        'PARENT_NETPROFIT': 'NET_PROFIT', 
        'SJLTZ': 'YoY_NET_PROFIT', 
        'SJLHZ': 'SEQUENTIAL_NET_PROFIT', 
        'BPS': 'NET_ASSET_PER_SHARE', 
        'WEIGHTAVG_ROE': 'RETURN_ON_NET_ASSET', 
        'MGJYXJJE': 'OPERATION_CASH_FLOW_PER_SHARE', 
        'XSMLL': 'GROSS_PROFIT_MARGIN', 
        'QDATE': 'DATE', 
        'PUBLISHNAME': 'INDUSTRY_NAME'
    }
    df=df[list(cols.keys())].rename(columns=cols)
    df["DATE"] = df["DATE"].apply(lambda x: trans_date(x))
    return df

def get_report_date(code):
    """
    获取东方财富财报单季度报日期
    https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/lrbDateAjaxNew?companyType=4&reportDateType=2&code=SZ002594
    """
    code = get_code_id(code, mode=2)
    url = "https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/lrbDateAjaxNew"
    params = {
        "companyType": 4,
        "reportDateType": 2,
        "code": code        
    }
    res = requests.get(url, params=params)
    return res.json()["data"]

def income_profit_statement_k10(code= None, page_num=8):
    """
    获取东方财富利润表
    http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/xjllbAjaxNew?companyType=4&reportDateType=0&reportType=2&dates=2023-03-31%2C2022-12-31%2C2022-09-30%2C2022-06-30%2C2022-03-31&code=SZ002594
    """
    dates = get_report_date(code)[:page_num]
    dates = ",".join(d["REPORT_DATE"][:10] for d in dates)
    code = get_code_id(code, mode=2)

    url = "http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/xjllbAjaxNew"
    params = {
        "companyType": 4,
        "reportDateType": 0,
        "reportType": 2,
        "dates": dates,
        "code": code,
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    return data_json

def income_profit_statement(code= None, latest=False, page_num=8):
    """
    获取东方财富利润表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    """
    #print(code)
    if latest:
        page_num = 1
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1",
        "pageSize": str(page_num),
        "pageNumber": "1",
        "reportName": "RPT_DMSK_FN_INCOME",
        "columns": "ALL",
        "filter": f"""(SECURITY_CODE={code})""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    df = pd.DataFrame(data_json["result"]["data"])

    cols = {
        "SECURITY_CODE": "SECURITY_CODE",
        "SECURITY_NAME_ABBR": "SECURITY_NAME",
        "INDUSTRY_NAME": "INDUSTRY_NAME",
        "REPORT_DATE": "DATE",
        "PARENT_NETPROFIT": "PARENT_NET_PROFIT",
        "TOTAL_OPERATE_INCOME": "TOTAL_OPERATE_INCOME",
        "TOTAL_OPERATE_COST": "TOTAL_OPERATE_COST", 
        "OPERATE_EXPENSE": "OPERATE_EXPENSE",
        "SALE_EXPENSE": "SALE_EXPENSE",
        "MANAGE_EXPENSE": "MANAGE_EXPENSE",
        "FINANCE_EXPENSE": "FINANCE_EXPENSE",
        "OPERATE_PROFIT": "OPERATE_PROFIT",
        "TOTAL_PROFIT": "TOTAL_PROFIT",
        "INCOME_TAX": "INCOME_TAX",
        "OPERATE_PROFIT_RATIO": "YoY_OPERATE_PROFIT",
        "DEDUCT_PARENT_NETPROFIT": "DEDUCT_NONPARENT_NETPROFIT",
        "PARENT_NETPROFIT_RATIO": "YoY_PARENT_NETPROFIT",
        "DPN_RATIO": "YoY_DEDUCTED_NONPARENT_NET_PROFIT",
        "TOE_RATIO": "YoY_TOTAL_OPERATE_COST",
        "TOI_RATIO": "YoY_TOTAL_OPERATE_INCOME"
    }
    df=df[list(cols.keys())].rename(columns=cols)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    return df

# RPT_DMSK_FN_CASHFLOW 现金流表
def cashflow_statement(date= None):
    """
    获取东方财富年报季报现金流量表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    date: 如"2022-03-31", "2022-06-30"
    """
    date=trans_date(date)
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "NOTICE_DATE,SECURITY_CODE",
        "sortTypes": "-1,-1",
        "pageSize": "500",
        "pageNumber": "1",
        "reportName": "RPT_DMSK_FN_CASHFLOW",
        "columns": "ALL",
        "filter": f"""(SECURITY_TYPE_CODE in ("058001001","058001008"))(TRADE_MARKET_CODE!="069001017")(REPORT_DATE='{date}')""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    page_num = data_json["result"]["pages"]
    df = pd.DataFrame()
    for page in tqdm(range(1, page_num + 1), leave=False):
        params.update(
            {
                "pageNumber": page,
            }
        )
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)
        time.sleep(1)
    cols = {
        "SECURITY_CODE": "SECURITY_CODE",
        "SECURITY_NAME_ABBR": "SECURITY_NAME",
        "INDUSTRY_NAME": "INDUSTRY_NAME",
        "REPORT_DATE": "DATE",        
        "CCE_ADD": "NET_CASH_FLOW",
        "CCE_ADD_RATIO": "YoY_NET_CASH_FLOW",
        "NETCASH_OPERATE": "OPERATING_NET_CASH_FLOW",
        "NETCASH_OPERATE_RATIO": "YoY_OPERATING_NET_CASH_FLOW",
        "NETCASH_INVEST": "NET_CASH_FROM_INVEST",
        "NETCASH_INVEST_RATIO": "YoY_NET_CASH_FROM_INVEST",
        "SALES_SERVICES": "CASH_FROM_SALES",
        "SALES_SERVICES_RATIO": "YoY_CASH_FROM_SALES",
        "PAY_STAFF_CASH": "PAY_STAFF_CASH",
        "PSC_RATIO": "YoY_PAY_STAFF_CASH",
        "RECEIVE_INVEST_INCOME": "CASH_INCOME_INVEST",
        "RII_RATIO": "YoY_CASH_INCOME_INVEST",
        "NETCASH_FINANCE": "NET_CASH_FLOW_FINANCIAL",
        "NETCASH_FINANCE_RATIO": "YoY_NET_CASH_FLOW_FINANCIAL",
        "CONSTRUCT_LONG_ASSET": "PAY_CONSTRUCTION_CASH",
        "CLA_RATIO": "YoY_PAY_CONSTRUCTION_CASH"
    }
    df=df[list(cols.keys())].rename(columns=cols)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    return df

def forcast_report(date = None) :
    """东方财富业绩预告
    https://data.eastmoney.com/bbsj/202003/yjyg.html
    date: 如"2022-03-31", "2022-06-30"
    """
    date=trans_date(date)
    url = "http://datacenter.eastmoney.com/securities/api/data/v1/get"
    params = {
        "sortColumns": "NOTICE_DATE,SECURITY_CODE",
        "sortTypes": "-1,-1",
        "pageSize": "50",
        "pageNumber": "1",
        "reportName": "RPT_PUBLIC_OP_NEWPREDICT",
        "columns": "ALL",
        "token": "894050c76af8597a853f5b408b759f5d",
        "filter": f" (REPORT_DATE='{date}')",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    #print(data_json)
    df = pd.DataFrame()
    total_page = data_json["result"]["pages"]
    #total_page = 1
    for page in tqdm(range(1, total_page + 1), leave=False):
        params = {
            "sortColumns": "NOTICE_DATE,SECURITY_CODE",
            "sortTypes": "-1,-1",
            "pageSize": "50",
            "pageNumber": page,
            "reportName": "RPT_PUBLIC_OP_NEWPREDICT",
            "columns": "ALL",
            "token": "894050c76af8597a853f5b408b759f5d",
            "filter": f" (REPORT_DATE='{date}')",
        }
        r = requests.get(url, params=params)
        data_json = r.json()
        #print(data_json)        
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.reset_index(inplace=True)
    df["index"] = range(1, len(df) + 1)

    cols = [
        "SECURITY_CODE", 
        "SECURITY_NAME_ABBR",
        "NOTICE_DATE",
        "REPORT_DATE",
        "PREDICT_FINANCE_CODE",
        "PREDICT_FINANCE",
        "ADD_AMP_LOWER",
        "ADD_AMP_UPPER",
        "PREDICT_RATIO_LOWER",
        "PREDICT_RATIO_UPPER"]

    df = df[cols].rename(
        columns={
            "SECURITY_NAME_ABBR": "SECURITY_NAME",
            "REPORT_DATE": "DATE",
            "ADD_AMP_LOWER": "QUARTER_ON_QUARTER_LOWER",
            "ADD_AMP_UPPER": "QUARTER_ON_QUARTER_UPPER",
            "PREDICT_RATIO_LOWER": "YoY_LOWER",
            "PREDICT_RATIO_UPPER": "YoY_UPPER"
        }
    )
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    df["NOTICE_DATE"] = df["NOTICE_DATE"].apply(lambda x: x[:10])
    return df

def eps_forecast():
    """
    获取东方财富网上市公司机构研报评级和每股收益预测
    http://data.eastmoney.com/report/profitforecast.jshtml
    """
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        'reportName': 'RPT_WEB_RESPREDICT',
        'columns': 'WEB_RESPREDICT',
        'pageNumber': '1',
        'pageSize': '500',
        'sortTypes': '-1',
        'sortColumns': 'RATING_ORG_NUM',
        'p': '1',
        'pageNo': '1',
        'pageNum': '1',
        'filter': '',
        '_': '1640241417037',
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    page_num = int(data_json['result']['pages'])
    df = pd.DataFrame()
    for page in tqdm(range(1, page_num + 1), leave=False):
        params.update({
            'pageNumber': page,
            'p': page,
            'pageNo': page,
            'pageNum': page,
        })
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json['result']['data'])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.reset_index(inplace=True)
    df["index"] = range(1, len(df) + 1)

    cols = [
        "SECURITY_CODE",
        "SECURITY_NAME_ABBR",
        "RATING_ORG_NUM",
        "RATING_BUY_NUM",
        "RATING_ADD_NUM",
        "YEAR1",
        "EPS1",
        "YEAR2",
        "EPS2",
        "YEAR3",
        "EPS3",
        "INDUSTRY_BOARD",
        "REGION_BOARD"
    ]
    df = df[cols].rename(columns = {
        "SECURITY_NAME_ABBR": "SECURITY_NAME"
    })
    return df

def stock_divide(code=None):
    """
    获取公司分红
    https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123028434509340504044_1692093275804&sortColumns=REPORT_DATE&sortTypes=-1&pageSize=50&pageNumber=1&reportName=RPT_SHAREBONUS_DET&columns=ALL&quoteColumns=&js=%7B%22data%22%3A(x)%2C%22pages%22%3A(tp)%7D&source=WEB&client=WEB&filter=(SECURITY_CODE%3D%22600519%22)    
    """
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        'reportName': 'RPT_SHAREBONUS_DET',
        'columns': 'ALL',
        'pageNumber': '1',
        'pageSize': '3',
        'sortTypes': '-1',
        'sortColumns': 'REPORT_DATE',
        'quoteColumns': '',
        'pageNo': '1',
        'pageNum': '1',
        "filter": f"""(SECURITY_CODE={code})""",
        'js': 'js={"data":(x),"pages":(tp)}',
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    df = pd.DataFrame(data_json["result"]["data"])
    cols = {
        "SECURITY_CODE": "SECURITY_CODE",
        "SECURITY_NAME_ABBR": "SECURITY_NAME",
        "PRETAX_BONUS_RMB": "PRE_TAX_BONUS_RMB",
        "DIVIDENT_RATIO": "DIVIDENT_PERCENT",
        "EQUITY_RECORD_DATE": "DATE"
    }
    df = df[list(cols.keys())].rename(columns=cols)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    df["DIVIDENT_PERCENT"] = df["DIVIDENT_PERCENT"].apply(lambda x: x*100)

    return df

###机构评级和每股收益预测

def stock_holder_num(date=None):
    """获取沪深A股最新公开的股东数量
    date : 默认最新的报告期,
    指定某季度如'2022-03-31','2022-06-30','2022-09-30','2022-12-31'
    """
    date = trans_date(date)
    dfs = []
    page = 1
    cols = {
        'SECURITY_CODE': 'SECURITY_CODE',
        'SECURITY_NAME_ABBR': 'SECURITY_NAME',
        'END_DATE': 'DATE',
        'HOLDER_NUM': 'HOLDER_NUM',
        'HOLDER_NUM_RATIO': 'PERCENT_HOLDER_NUM_CHANGE',
        'HOLDER_NUM_CHANGE': 'HOLDER_NUM_CHANGE',
        'AVG_MARKET_CAP': 'CAPITAL_PER_HOLDER',
        'AVG_HOLD_NUM': 'STOCK_NUM_PER_HOLDER',
        "TOTAL_MARKET_CAP": "TOTAL_MARKET_VALUE",
        "TOTAL_A_SHARES": "TOTAL_SHARE",
    }

    while True:
        params = [
            ('sortColumns', 'HOLD_NOTICE_DATE,SECURITY_CODE'),
            ('sortTypes', '-1,-1'),
            ('pageSize', '500'),
            ('pageNumber', page),
            ('columns',
             'SECURITY_CODE,SECURITY_NAME_ABBR,END_DATE,INTERVAL_CHRATE,AVG_MARKET_CAP,AVG_HOLD_NUM,TOTAL_MARKET_CAP,TOTAL_A_SHARES,HOLD_NOTICE_DATE,HOLDER_NUM,PRE_HOLDER_NUM,HOLDER_NUM_CHANGE,HOLDER_NUM_RATIO,END_DATE,PRE_END_DATE'),
            ('quoteColumns', 'f2,f3'),
            ('source', 'WEB'),
            ('client', 'WEB'),
        ]
        if date is not None:
            params.append(('filter', f'(END_DATE=\'{date}\')'))
            params.append(('reportName', 'RPT_HOLDERNUM_DET'))
        else:
            params.append(('reportName', 'RPT_HOLDERNUMLATEST'))

        params = tuple(params)
        url = 'http://datacenter-web.eastmoney.com/api/data/v1/get'
        response = session.get(url,
                               headers=request_header,
                               params=params)
        items = jsonpath(response.json(), '$..data[:]')
        if not items:
            break
        df = pd.DataFrame(items)
        page += 1
        dfs.append(df)
    if len(dfs) == 0:
        df = pd.DataFrame(columns=fields.keys())        
        return df
    df = pd.concat(dfs, ignore_index=True)
    df=df[list(cols.keys())].rename(columns=cols)
    df["DATE"] = df["DATE"].apply(lambda x: x[:10])
    return df


def main_business(code="000001"):
    """## chinese: 获取公司主要业务|公司业务
    ## english: Get main business of compnay|main business
    ## args:
        code: 股票名称
    ## extra: http://f10.emoney.cn/f10/zbyz/1000001
    """
    try:
        code = code.strip()
        if not code.isdigit():
            code=stock_code_dict()[code]
        url = f"http://f10.emoney.cn/f10/zygc/{code}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        year_list = [item.text.strip()
            for item in soup.find(attrs={"class": "swlab_t"}).find_all("li")]

        df = pd.DataFrame()
        all_cols = {
            "报告期": "DATE",
            "分类方向": "DIRECTION",
            "分类": "CATEGORY",
            "营业收入(元)": "INCOME",
            "同比增长": "YoY_INCOME",
            "占主营收入比": "PERCENT_INCOME",
            "营业成本(元)": "COST",
            "同比增长.1": "YoY_COST",
            "占主营成本比": "PERCENT_COST",
            "毛利率": "GROSS_PROFIT_MARGIN",
            "同比增长.2": "YoY_GROSS_PROFIT_MARGIN"
        }
        for i, item in enumerate(year_list, 2):
            temp_df = pd.read_html(res.text, header=0)[i]
            #print(temp_df)
            temp_df.columns = [
                "分类方向",
                "分类",
                "营业收入(元)",
                "同比增长",
                "占主营收入比",
                "营业成本(元)",
                "同比增长.1",
                "占主营成本比",
                "毛利率",
                "同比增长.2",
            ]
            temp_df["报告期"] = item
            df = pd.concat([df, temp_df], ignore_index=True)

        df[['营业收入(元)','营业成本(元)']]=df[['营业收入(元)','营业成本(元)']
                                    ].apply(lambda s:s.str.strip('亿'))
        cols= ["同比增长",
                "占主营收入比",
                "同比增长.1",
                "占主营成本比",
                "毛利率",
                "同比增长.2",]

        df[cols]=df[cols].apply(lambda s:s.str.strip('%'))
        ignore_cols = ["报告期","分类方向","分类",'营业收入(元)','营业成本(元)']
        df = trans_num(df, ignore_cols)
        df["报告期"] = df["报告期"].apply(lambda x: trans_date(x))
        df=df[list(all_cols.keys())].rename(columns=all_cols)
        return df
    except Exception as e: 
        print(e)
        return ""

def daily_money_flow(code):
    """## chinese: 获取公司流入流出|股票天级流动情况
    ## english: Get daily moneyflow of stock|daily moneyflow
    ## args: 
        code: 股票名称 
    ## extra:  
        https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery112305477231164992162_1687338713166&reportName=PRT_STOCK_CAPITALFLOWS&columns=ALL&filter=(SECUCODE%3D%22300418.SZ%22)&pageNumber=1&pageSize=1&sortTypes=-1&sortColumns=TRADE_DATE&source=WEB&client=WEB&_=1687338713167
    """
    try:
        code_id = get_code_id(code, 2)
        url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
        params = {
            "sortColumns": "TRADE_DATE",
            "sortTypes": "-1",
            "pageSize": "1",
            "pageNumber": "1",
            "reportName": "PRT_STOCK_CAPITALFLOWS",
            "columns": "ALL",
            "source": "WEB",
            "client": "WEB",
            "filter": f'(SECUCODE="{code_id}")',
            '_': '1687338713167',
        }
        res = requests.get(url, params=params)
        data_json = res.json()
        df = pd.DataFrame(data_json['result']['data'])
        df["SECUCODE"]=df["SECUCODE"].apply(lambda s: s[:-3])
        df["TRADE_DATE"]=df["TRADE_DATE"].apply(lambda s: s[:10])        
        df = df.rename(columns={
            "SECUCODE": "SECURITY_CODE",
            "TRADE_DATE": "DATE",
            "BOARD_NAME": "INDUSTRY_NAME",
            })
        return df
    except:
        return None

###############################################################################

#######

###########################################################
###  whole file need to rewrite, only for data storage  ###
###########################################################

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

def stock_holder_change():
    """获取大股东增减持变动明细
    """
    url = 'https://datacenter-web.eastmoney.com/api/data/v1/get'
    params = {
        'sortColumns': 'END_DATE,SECURITY_CODE,EITIME',
        'sortTypes': '-1,-1,-1',
        'pageSize': '500',
        'pageNumber': '1',
        'reportName': 'RPT_SHARE_HOLDER_INCREASE',
        'quoteColumns': 'f2~01~SECURITY_CODE~NEWEST_PRICE,f3~01~SECURITY_CODE~CHANGE_RATE_QUOTES',
        'columns': 'ALL',
        'source': 'WEB',
    }
    r = requests.get(url, params=params)
    data_json = r.json()
    total_page = data_json['result']['pages']
    df = pd.DataFrame()
    for page in tqdm(range(1, total_page+1), leave=False):
        params.update({
            'pageNumber': page,
        })
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json['result']['data'])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.columns = ['变动数量','公告日','代码','股东名称',
        '变动占总股本比例','_','-','截止日','-',
        '变动后持股总数','变动后占总股本比例','_',
        '变动后占流通股比例','变动后持流通股数','_',
        '名称','增减','_','变动占流通股比例','开始日',
        '_', '最新价','涨跌幅','_',]

    df = df[['代码','名称','最新价','涨跌幅','股东名称','增减',
        '变动数量','变动占总股本比例','变动占流通股比例',
        '变动后持股总数','变动后占总股本比例','变动后持流通股数',
        '变动后占流通股比例','开始日','截止日','公告日',]]
    df['开始日'] = pd.to_datetime(df['开始日']).dt.date
    df['截止日'] = pd.to_datetime(df['截止日']).dt.date
    df['公告日'] = pd.to_datetime(df['公告日']).dt.date
   
    cols = ['代码', '名称', '股东名称','增减','开始日','截止日','公告日',]
    df = trans_num(df, cols).round(2)
    return df


# 个股或债券或期货历史资金流向数据
def daily_money(code):
    """## chinese: 获取股票天级流入流出数据|天级股票流入流出|资金流入流出
    ## english: Get incoming or outcoming of stock
    ## args: 
        code: 股票名称 
    ## extra:  
        pass
    """
    history_money_dict = {
        'f51': '日期',
        'f52': '主力净流入',
        'f53': '小单净流入',
        'f54': '中单净流入',
        'f55': '大单净流入',
        'f56': '超大单净流入',
        'f57': '主力净流入占比',
        'f58': '小单流入净占比',
        'f59': '中单流入净占比',
        'f60': '大单流入净占比',
        'f61': '超大单流入净占比',
        'f62': '收盘价',
        'f63': '涨跌幅'}

    fields = list(history_money_dict.keys())
    columns = list(history_money_dict.values())
    fields2 = ",".join(fields)
    code_id = get_code_id(code)
    if not code_id:
        return "Not Found Data"    
    params = (
        ('lmt', '30'),
        ('klt', '101'),
        ('secid', code_id),
        ('fields1', 'f1,f2,f3,f7'),
        ('fields2', fields2),
    )
    url = 'http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get'
    res = session.get(url,
                      headers=request_header,
                      params=params).json()

    data = jsonpath(res, '$..klines[:]')
    if not data:
        columns.insert(0, '代码')
        columns.insert(0, '名称')
        return pd.DataFrame(columns=columns)
    rows = [d.split(',') for d in data]
    name = jsonpath(res, '$..name')[0]
    code = code_id.split('.')[-1]
    df = pd.DataFrame(rows, columns=columns)
    df.insert(0, '代码', code)
    df.insert(0, '名称', name)
    cols = ['代码', '名称', '日期']
    df = trans_num(df, cols)
    return df