# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:53:48 2022

"""
import pandas as pd
import requests
import calendar
from datetime import datetime
from jsonpath import jsonpath
from tqdm import tqdm
from bs4 import BeautifulSoup
import time
from openfinance.datacenter.database.source.eastmoney.trade import market_realtime
from openfinance.datacenter.database.source.eastmoney.util import (
    latest_report_date,
    trans_num,
    get_code_id,
    request_header, 
    session,
)

###########################################################
###  whole file need to rewrite, only for data storage  ###
###########################################################

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

##########################################################################
def institute_hold(quarter = "20221"):
    """获取机构持股
    http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml
    quarter: 如'20221表示2022年一季度，
    其中的 1 表示一季报; "20193", 其中的 3 表示三季报;
    """
    url = "http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml?symbol=%D6%A4%C8%AF%BC%F2%B3%C6%BB%F2%B4%FA%C2%EB"
    params = {
        "p": "1",
        "num": "5000",
        "reportdate": quarter[:-1],
        "quarter": quarter[-1],
    }
    res = requests.get(url, params=params)
    df = pd.read_html(res.text)[0]
    df["证券代码"] = df["证券代码"].astype(str).str.zfill(6)
    del df["明细"]
    df.columns = ['证券代码', '简称', '机构数', '机构数变化', '持股比例', '持股比例增幅', '占流通股比例', '占流通股比例增幅']
    return df

def financial_statement(flag='业绩报表',date=None):
    """获取财务报表和业绩指标
    flag:报表类型,默认输出业绩报表，注意flag或date输出也默认输出业绩报表
    '业绩报表'或'yjbb'：返回年报季报财务指标
    '业绩快报'或'yjkb'：返回市场最新业绩快报
    '业绩预告'或'yjyg'：返回市场最新业绩预告
    '资产负债表'或'zcfz'：返回最新资产负债指标
    '利润表'或'lrb'：返回最新利润表指标
    '现金流量表'或'xjll'：返回最新现金流量表指标
    date:报表日期，如‘20220630’，‘20220331’，默认当前最新季报（或半年报或年报）
    """
    date=trans_date(date)
    if flag in ['业绩快报','yjkb']:
        return stock_yjkb(date)
    
    elif flag in ['业绩预告','yjyg']:
        return stock_yjyg(date)
    
    elif flag in ['资产负债表','资产负债','zcfz','zcfzb']:
        return balance_sheet(date)
    
    elif flag in ['利润表','利润' ,'lr' ,'lrb']:
        return income_statement(date)
    
    elif flag in ['现金流量表','现金流量' ,'xjll' ,'xjllb']:
        return cashflow_statement(date)
    
    else:
        return stock_yjbb(date)

#资产负债表
def trans_date(date=None):
    '''将日期格式'2022-09-30'转为'20220930'
    '''
    if date is None:
        date=latest_report_date()
    date=''.join(date.split('-'))
    return date
    
def balance_sheet(date= None):
    """获取年报季报资产负债表
    http://data.eastmoney.com/bbsj/202003/zcfz.html
    date:如"20220331", "20220630",
    """
    date=trans_date(date)
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "NOTICE_DATE,SECURITY_CODE",
        "sortTypes": "-1,-1",
        "pageSize": "500",
        "pageNumber": "1",
        "reportName": "RPT_DMSK_FN_BALANCE",
        "columns": "ALL",
        "filter": f"""(SECURITY_TYPE_CODE in ("058001001","058001008"))(TRADE_MARKET_CODE!="069001017")(REPORT_DATE='{'-'.join([date[:4], date[4:6], date[6:]])}')""",
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
    df.columns = ["序号", "_","代码","_","_","简称", "_","_","_","_", "_","_",
        "_","公告日","_","总资产","_","货币资金","_","应收账款","_","存货","_",
        "总负债","应付账款","_","预收账款","_","股东权益","_","总资产同比","总负债同比",
        "_","资产负债率","_","_","_","_","_","_","_","_","_","_","_","_","_","_",
        "_","_","_","_", "_","_","_","_","_","_",]
    df = df[["代码", "简称","货币资金","应收账款","存货","总资产", "总资产同比",
            "应付账款","预收账款","总负债","总负债同比","资产负债率","股东权益","公告日",]]
    df["公告日"] = pd.to_datetime(df["公告日"]).dt.date
    cols = ['代码', '简称', '公告日',]
    df = trans_num(df, cols).round(2)
    return df

def income_statement(date = None):
    """
    获取东方财富年报季报-利润表
    http://data.eastmoney.com/bbsj/202003/lrb.html
    date: 如"20220331", "20220630"
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
        "filter": f"""(SECURITY_TYPE_CODE in ("058001001","058001008"))(TRADE_MARKET_CODE!="069001017")(REPORT_DATE='{'-'.join([date[:4], date[4:6], date[6:]])}')""",
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
def balance_sheet_statement(code= None):
    """
    获取东方财富业绩报表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    date: 如"20220331", "20220630"
    """
    #date=trans_date(date)
    #print(code)
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1",
        "pageSize": "50",
        "pageNumber": "1",
        "reportName": "RPT_DMSK_FN_BALANCE",
        "columns": "ALL",
        "filter": f"""(SECURITY_CODE={code})""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    #print(data_json)
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
        
    return df

def financial_report_statement(code= None):
    """
    获取东方财富业绩报表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    date: 如"20220331", "20220630"
    """
    #date=trans_date(date)
    #print(code)
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "REPORTDATE",
        "sortTypes": "-1",
        "pageSize": "50",
        "pageNumber": "1",
        "reportName": "RPT_LICO_FN_CPD",
        "columns": "ALL",
        "filter": f"""(SECURITY_CODE={code})""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    #print(data_json)
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

    fields = [
        "SECURITY_CODE",
        "SECURITY_NAME_ABBR",
        "TOTAL_OPERATE_INCOME",
        "YSTZ",
        "YSHZ",
        "PARENT_NETPROFIT",
        "SJLTZ",
        "SJLHZ",
        "BPS",
        "WEIGHTAVG_ROE",
        "MGJYXJJE",
        "XSMLL",
        "QDATE",
        "PUBLISHNAME"
    ]
    df = df[fields]
    new_names = [
        "code",
        "name",
        "TOTAL_OPERATE_INCOME",
        "YoY_Revenue",
        "Sequential_revenue",
        "NET_PROFIT",
        "YoY_NET_PROFIT",
        "Sequential_NET_PROFIT",
        "Net_assets_per_share",
        "Return_on_net_assets",
        "Operating_cash_flow_per_share",
        "gross_profit_rate",
        "QDATE",
        "PUBLISHNAME"        
    ]
    df=df[fields].rename(columns=dict(zip(fields,new_names)))
    return df


def income_profit_statement(code= None):
    """
    获取东方财富利润表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    date: 如"20220331", "20220630"
    """
    #date=trans_date(date)
    #print(code)
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    params = {
        "sortColumns": "REPORT_DATE",
        "sortTypes": "-1",
        "pageSize": "50",
        "pageNumber": "1",
        "reportName": "RPT_DMSK_FN_INCOME",
        "columns": "ALL",
        "filter": f"""(SECURITY_CODE={code})""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    #print(data_json) 
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

    fields = [
        "SECURITY_CODE",
        "SECURITY_NAME_ABBR",
        "INDUSTRY_NAME",
        "PARENT_NETPROFIT",
        "TOTAL_OPERATE_INCOME",
        "TOTAL_OPERATE_COST",
        "TOE_RATIO",
        "OPERATE_COST",
        "OPERATE_EXPENSE",
        "SALE_EXPENSE",
        "MANAGE_EXPENSE",
        "FINANCE_EXPENSE",
        "OPERATE_PROFIT",
        "TOTAL_PROFIT",
        "INCOME_TAX",
        "TOI_RATIO",
        "OPERATE_PROFIT_RATIO",
        "PARENT_NETPROFIT_RATIO",
        "DPN_RATIO",
        "REPORT_DATE"
    ]
    df = df[fields]
    new_names = [
        "SECURITY_CODE",
        "SECURITY_NAME_ABBR",
        "INDUSTRY_NAME",
        "PARENT_NETPROFIT",
        "TOTAL_OPERATE_INCOME",
        "TOTAL_OPERATE_COST",
        "TOTAL_OPERATE_EXPENSE_RATIO",
        "OPERATE_COST",
        "OPERATE_EXPENSE",
        "SALE_EXPENSE",
        "MANAGE_EXPENSE",
        "FINANCE_EXPENSE",
        "OPERATE_PROFIT",
        "TOTAL_PROFIT",
        "INCOME_TAX",
        "TOTAL_OPERATE_INCOME_RATIO",
        "OPERATE_PROFIT_RATIO",
        "PARENT_NETPROFIT_RATIO",
        "Recurring_Net_PARENT_NETPROFIT_RATIO",
        "REPORT_DATE"          
    ]
    df=df[fields].rename(columns=dict(zip(fields,new_names)))
    return df

# RPT_DMSK_FN_CASHFLOW 现金流表
def cashflow_statement(date= None):
    """
    获取东方财富年报季报现金流量表
    http://data.eastmoney.com/bbsj/202003/xjll.html
    date: 如"20220331", "20220630"
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
        "filter": f"""(SECURITY_TYPE_CODE in ("058001001","058001008"))(TRADE_MARKET_CODE!="069001017")(REPORT_DATE='{'-'.join([date[:4], date[4:6], date[6:]])}')""",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    page_num = data_json["result"]["pages"]
    #page_num = 2
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
    '''
    df.reset_index(inplace=True)
    df["index"] = df.index + 1

    df.columns = ["序号","_","代码","_","_","简称","_","_","_","_","_","_","_",
        "公告日","_","经营性现金流量净额","经营性净现金流占比","_","_","_","_",
        "投资性现金流量净额","投资性净现金流占比","_","_","_","_",
        "融资性现金流量净额","融资性净现金流占比","净现金流",
        "净现金流同比增长","_","_","_","_","_","_","_","_","_","_","_","_",
        "_","_", "_","_","_","_",]

    fields =["代码","简称","净现金流","净现金流同比增长","经营性现金流量净额",
            "经营性净现金流占比","投资性现金流量净额", "投资性净现金流占比",
            "融资性现金流量净额","融资性净现金流占比","公告日"]
    
    df = df[fields]
    df["公告日"] = pd.to_datetime(df["公告日"]).dt.date
    cols = ['代码', '简称', '公告日',]
    df = trans_num(df, cols).round(2)
    new_names = [
        "code",    
        "abbre",    
        "net_cash_flow",
        "YOY_growth_of_net_cash_flow",
        "net_operating_cash_flow",
        "Proportion_of_net_operating_cash_flow",  
        "net_cash_flow_from_investment_activities",
        "Proportion_of_net_cash_flow_from_investment_activities", 
        "net_cash_flow_from_financing_activities",   
        "Proportion_of_net_cash_flow_from_financing_activities",
        "announcement_date"       
    ]
    df=df[fields].rename(columns=dict(zip(fields,new_names)))
    '''
    return df

def stock_yjkb(date= None):
    """获取东方财富年报季报-业绩快报
    http://data.eastmoney.com/bbsj/202003/yjkb.html
    date: 如"20220331", "20220630"
    """
    date=trans_date(date)
    url = "http://datacenter.eastmoney.com/api/data/get"
    params = {
        "st": "UPDATE_DATE,SECURITY_CODE",
        "sr": "-1,-1",
        "ps": "5000",
        "p": "1",
        "type": "RPT_FCI_PERFORMANCEE",
        "sty": "ALL",
        "token": "894050c76af8597a853f5b408b759f5d",
        "filter": f"(REPORT_DATE='{'-'.join([date[:4], date[4:6], date[6:]])}')",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    page_num = data_json["result"]["pages"]
    old_cols=["序号","代码","简称","板块", "_","类型","_","公告日","_",
            "每股收益","营业收入","营业收入去年同期","净利润","净利润去年同期",
            "每股净资产","净资产收益率","营业收入同比","净利润同比",
            "营业收入季度环比","净利润季度环比","行业","_","_","_","_","_",
            "_","_","_",]
    new_cols= ["代码","简称","每股收益","营业收入", "营业收入去年同期", 
                   "营业收入同比","营业收入季度环比","净利润","净利润去年同期", 
                   "净利润同比","净利润季度环比","每股净资产","净资产收益率",
                   "行业","公告日","板块","类型",]
    
    if page_num > 1:
        df = pd.DataFrame()
        for page in tqdm(range(1, page_num + 1), leave=True):
            params = {
                "st": "UPDATE_DATE,SECURITY_CODE",
                "sr": "-1,-1",
                "ps": "5000",
                "p": page,
                "type": "RPT_FCI_PERFORMANCEE",
                "sty": "ALL",
                "token": "894050c76af8597a853f5b408b759f5d",
                "filter": f"(REPORT_DATE='{'-'.join([date[:4], date[4:6], date[6:]])}')",
            }
            r = requests.get(url, params=params)
            data_json = r.json()
            temp_df = pd.DataFrame(data_json["result"]["data"])
            temp_df.reset_index(inplace=True)
            temp_df["index"] = range(1, len(temp_df) + 1)
            df = pd.concat([df, temp_df], ignore_index=True)
        
        df.columns = old_cols
        df = df[new_cols]
        return df
    df2 = pd.DataFrame(data_json["result"]["data"])
    df2.reset_index(inplace=True)
    df2["index"] = range(1, len(df2) + 1)
    df2.columns = old_cols
    df2 = df2[new_cols]
    return df2


def stock_yjyg(date = None) :
    """东方财富业绩预告
    date: 如"20220331", "20220630"
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
        "filter": f" (REPORT_DATE='{'-'.join([date[:4], date[4:6], date[6:]])}')",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    df = pd.DataFrame()
    total_page = data_json["result"]["pages"]
    for page in tqdm(range(1, total_page + 1), leave=False):
        params = {
            "sortColumns": "NOTICE_DATE,SECURITY_CODE",
            "sortTypes": "-1,-1",
            "pageSize": "50",
            "pageNumber": page,
            "reportName": "RPT_PUBLIC_OP_NEWPREDICT",
            "columns": "ALL",
            "token": "894050c76af8597a853f5b408b759f5d",
            "filter": f" (REPORT_DATE='{'-'.join([date[:4], date[4:6], date[6:]])}')",
        }
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.reset_index(inplace=True)
    df["index"] = range(1, len(df) + 1)
    df.columns = ["序号","_","代码", "简称","_","公告日","报告日","_","预测指标",
        "_","_","_","_","业绩变动","变动原因","预告类型","上年同期","_","_",
        "_","_","变动幅度","预测数值","_","_",]
    df = df[["代码","简称","预测指标","业绩变动","预测数值","变动幅度",
            "变动原因","预告类型","上年同期","公告日",]]
    return df


def stock_yjbb(date= "20200331"):
    """
    东方财富年报季报业绩报表
    http://data.eastmoney.com/bbsj/202003/yjbb.html
    date: 如"20220331", "20220630"
    """
    date=trans_date(date)
    url = "http://datacenter.eastmoney.com/api/data/get"
    params = {
        "st": "UPDATE_DATE,SECURITY_CODE",
        "sr": "-1,-1",
        "ps": "5000",
        "p": "1",
        "type": "RPT_LICO_FN_CPD",
        "sty": "ALL",
        "token": "894050c76af8597a853f5b408b759f5d",
        "filter": f"(REPORTDATE='{'-'.join([date[:4], date[4:6], date[6:]])}')",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    page_num = data_json["result"]["pages"]
    df = pd.DataFrame()
    for page in tqdm(range(1, page_num + 1), leave=False):
        params = {
            "st": "UPDATE_DATE,SECURITY_CODE",
            "sr": "-1,-1",
            "ps": "500",
            "p": page,
            "type": "RPT_LICO_FN_CPD",
            "sty": "ALL",
            "token": "894050c76af8597a853f5b408b759f5d",
            "filter": f"(REPORTDATE='{'-'.join([date[:4], date[4:6], date[6:]])}')",
        }
        r = requests.get(url, params=params)
        data_json = r.json()
        temp_df = pd.DataFrame(data_json["result"]["data"])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.reset_index(inplace=True)
    df["index"] = range(1, len(df) + 1)
    df.columns = ["序号", "代码","简称","_","_","_","_","最新公告日","_","每股收益",
        "_","营业收入","净利润","净资产收益率","营业收入同比","净利润同比","每股净资产",
        "每股经营现金流量","销售毛利率","营业收入季度环比","净利润季度环比",
        "_","_","行业","_","_","_","_","_","_","_","_","_","_","_",]
    
    df = df[["代码","简称","每股收益","营业收入","营业收入同比","营业收入季度环比",
            "净利润","净利润同比","净利润季度环比","每股净资产","净资产收益率",
            "每股经营现金流量","销售毛利率","行业", "最新公告日",]]
    return df


def stock_code_dict():
    df=market_realtime()
    name_code=dict(df[['名称','代码']].values)
    return name_code

###机构评级和每股收益预测
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
    df["index"] = df.index + 1
    year1 = list(set(df['YEAR1']))[-1]
    year2 = list(set(df['YEAR2']))[-1]
    year3 = list(set(df['YEAR3']))[-1]
    year4 = list(set(df['YEAR4']))[0]
    df.columns = ["序号","-","代码","名称","研报数","买入","增持","中性","减持",
        "卖出","-","_",f"{year1}每股收益","-","_",f"{year2}每股收益","-","_",
        f"{year3}每股收益","-","_",f"{year4}每股收益","_","_","_","_","_","_",
        "_","_","_","_",]

    df = df[["代码","名称","研报数","买入","增持","中性","减持","卖出",
            f"{year1}每股收益",f"{year2}每股收益",
            f"{year3}每股收益",f"{year4}每股收益",]]
    
    ignore_cols = ['代码', '名称']
    df = trans_num(df, ignore_cols)
    return df


#########################################################################
def stock_holder(holder=None,date=None, code=None, n=2):
    """获取沪深市场指定股票的股东变动情况
    holder:股东类型：'实控人'，返回实控人持股变动情况，
           '高管'，返回高管持股变动情况，
           None,返回全市场个股股东增减持情况或某指定个股前十大股票变化情况
    date:日期，code:股票代码或简称
    默认参数下返回的是全市场个股最新日期的变动情况
    """
    
    if holder in [1,'实控人','con','controller','control','实际控制人','skr']:
        return stock_holder_con()
    
    elif holder in [2,'股东','股东增减持','股东持股','gd']:
        return stock_holder_change()
    
    else:
        if code is None:
            # 获取市场数据
            if date is not None and '-' not in date:
                date = '-'.join([date[:4], date[4:6], date[6:]])
            df = stock_holder_num(date)
            if len(df) < 1:
                df = stock_holder_num(latest_report_date())
            return df
        else:
            return stock_holder_top10(code, n)
        


def stock_holder_num(date=None):
    """获取沪深A股最新公开的股东数量
    date : 默认最新的报告期,
    指定某季度如'2022-03-31','2022-06-30','2022-09-30','2022-12-31'
    """

    if date is not None and '-' not in date:
        date_trans = lambda s: '-'.join([s[:4], s[4:6], s[6:]])
        date = date_trans(date)

    dfs = []
    if date is not None:
        date= datetime.strptime(date, '%Y-%m-%d')
        year = date.year
        month = date.month
        if month % 3 != 0:
            month -= month % 3
        if month < 3:
            year -= 1
            month = 12
        _, last_day = calendar.monthrange(year, month)
        date: str = datetime.strptime(
            f'{year}-{month}-{last_day}', '%Y-%m-%d').strftime('%Y-%m-%d')
    page = 1
    fields = {
        'SECURITY_CODE': '代码',
        'SECURITY_NAME_ABBR': '名称',
        'END_DATE': '截止日',
        'HOLDER_NUM': '股东人数',
        'HOLDER_NUM_RATIO': '增减(%)',
        'HOLDER_NUM_CHANGE': '较上期变化',
        'AVG_MARKET_CAP': '户均持股市值',
        'AVG_HOLD_NUM': '户均持股数量',
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
        #df = df.rename(columns=fields)[fields.values()]
        page += 1
        dfs.append(df)
    if len(dfs) == 0:
        #df = pd.DataFrame(columns=fields.values())
        df = pd.DataFrame(columns=fields.keys())        
        return df
    df = pd.concat(dfs, ignore_index=True)
    df['END_DATE'] = pd.to_datetime(df['END_DATE']).apply(lambda x: x.strftime('%Y%m%d'))
    cols = ['SECURITY_CODE', 'SECURITY_NAME_ABBR', 'END_DATE']
    df = trans_num(df, cols).round(2)
    return df

# 获取沪深市场股票某一季度的表现情况
def company_indicator(date=None):
    """
    获取沪深市场股票某一季度的表财务指标
    date报告发布日期，默认最新，如‘2022-09-30’
    一季度：‘2021-03-31’；二季度：'2021-06-30'
    三季度：'2021-09-30'；四季度：'2021-12-31'
    """
    if date is not None and '-' not in date:
        date_trans = lambda s: '-'.join([s[:4], s[4:6], s[6:]])
        date = date_trans(date)
    if date is None:
        date = latest_report_date()

    fields = {
        'SECURITY_CODE': '代码',
        'SECURITY_NAME_ABBR': '简称',
        'NOTICE_DATE': '公告日期',
        'TOTAL_OPERATE_INCOME': '营收',
        'YSTZ': '营收同比',
        'YSHZ': '营收环比',
        'PARENT_NETPROFIT': '净利润',
        'SJLTZ': '净利润同比',
        'SJLHZ': '净利润环比',
        'BASIC_EPS': '每股收益',
        'BPS': '每股净资产',
        'WEIGHTAVG_ROE': '净资产收益率',
        'XSMLL': '销售毛利率',
        'MGJYXJJE': '每股经营现金流'
    }

    date = f"(REPORTDATE=\'{date}\')"
    page = 1
    dfs = []
    while True:
        params = (
            ('st', 'NOTICE_DATE,SECURITY_CODE'),
            ('sr', '-1,-1'),
            ('ps', '500'),
            ('p', f'{page}'),
            ('type', 'RPT_LICO_FN_CPD'),
            ('sty', 'ALL'),
            ('token', '894050c76af8597a853f5b408b759f5d'),
            # 沪深A股
            ('filter',
             f'(SECURITY_TYPE_CODE in ("058001001","058001008")){date}'),

        )
        url = 'http://datacenter-web.eastmoney.com/api/data/get'
        response = session.get(url,
                               headers=request_header,
                               params=params)
        items = jsonpath(response.json(), '$..data[:]')
        if not items:
            break
        df = pd.DataFrame(items)
        dfs.append(df)
        page += 1
    if len(dfs) == 0:
        df = pd.DataFrame(columns=fields.values())
        return df
    df = pd.concat(dfs, axis=0, ignore_index=True)
    df = df.rename(columns=fields)[fields.values()]
    cols = ['代码', '简称', '公告日期']
    df = trans_num(df, cols).round(3)
    return df