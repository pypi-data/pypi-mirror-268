#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2022/9/29 20:28 
'''
import re
import time
import datetime
import requests
import pandas as pd
from retry.api import retry
from jsonpath import jsonpath
from pathlib import Path
from py_mini_racer import py_mini_racer

# 东方财富网网页请求头
request_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'}

session = requests.Session()

trade_detail_dict = {
    'f12': '代码',
    'f14': '名称',
    'f3': '涨幅',
    'f2': '最新',
    'f15': '最高',
    'f16': '最低',
    'f17': '今开',
    'f8': '换手率',
    'f10': '量比',
    'f115': '市盈率TTM',
    'f5': '成交量',
    'f6': '成交额',
    'f18': '昨收',
    'f20': '总市值',
    'f21': '流通市值',
    'f13': '编号',
    'f124': '更新时间戳',
}

# 市场与编码
market_dict = {
    'stock': 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23',
    '沪深A': 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23',
    '上证A': 'm:1 t:2,m:1 t:23',
    '沪A': 'm:1 t:2,m:1 t:23',
    '深证A': 'm:0 t:6,m:0 t:80',
    '深A': 'm:0 t:6,m:0 t:80',
    '北证A': 'm:0 t:81 s:2048',
    '北A': 'm:0 t:81 s:2048',
    '创业板': 'm:0 t:80',
    '科创板': 'm:1 t:23',
    '沪深京A': 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048',
    '沪股通': 'b:BK0707',
    '深股通': 'b:BK0804',
    '风险警示板': 'm:0 f:4,m:1 f:4',
    '两网及退市': 'm:0 s:3',
    '新股': 'm:0 f:8,m:1 f:8',
    '美股': 'm:105,m:106,m:107',
    '港股': 'm:128 t:3,m:128 t:4,m:128 t:1,m:128 t:2',
    '英股': 'm:155 t:1,m:155 t:2,m:155 t:3,m:156 t:1,m:156 t:2,m:156 t:5,m:156 t:6,m:156 t:7,m:156 t:8',
    '中概股': 'b:MK0201',
    '中国概念股': 'b:MK0201',
    '地域板块': 'm:90 t:1 f:!50',
    '行业板块': 'm:90 t:2 f:!50',
    '概念板块': 'm:90 t:3 f:!50',
    '上证指数': 'm:1 s:2',
    '上证系列指数': 'm:1 s:2',
    '深证指数': 'm:0 t:5',
    '深证系列指数': 'm:0 t:5',
    '沪深指数': 'm:1 s:2,m:0 t:5',
    '沪深系列指数': 'm:1 s:2,m:0 t:5',
    'bond': 'b:MK0354',
    '债券': 'b:MK0354',
    '可转债': 'b:MK0354',
    'future': 'm:113,m:114,m:115,m:8,m:142',
    '期货': 'm:113,m:114,m:115,m:8,m:142',
    'fund': 'b:MK0021,b:MK0022,b:MK0023,b:MK0024',
    'ETF': 'b:MK0021,b:MK0022,b:MK0023,b:MK0024',
    'LOF': 'b:MK0404,b:MK0405,b:MK0406,b:MK0407', 
}

# 市场编号
market_num_dict = {
    '0': '深A',
    '1': '沪A',
    '105': '美股',
    '106': '美股',
    '107': '美股',
    '116': '港股',
    '128': '港股',
    '113': '上期所',
    '114': '大商所',
    '115': '郑商所',
    '8': '中金所',
    '142': '上海能源期货交易所',
    '155': '英股',
    '90': '板块'
}

code_id_dict = {
    '上证综指': '1.000001', 'sh': '1.000001', '上证指数': '1.000001', '1.000001': '1.000001',
    '深证综指': '0.399106', 'sz': '0.399106', '深证指数': '0.399106', '深证成指': '0.399106',
    '创业板指': '0.399006', 'cyb': '0.399006', '创业板': '0.399006', '创业板指数': '0.399006',
    '沪深300': '1.000300', 'hs300': '1.000300',
    '上证50': '1.000016', 'sz50': '1.000016',
    '上证180': '1.000010', 'sz180': '1.000010',
    '科创50': '1.000688', 'kc50': '1.000688',
    '中小100': '0.399005', 'zxb': '0.399005', '中小板': '0.399005', '中小板指数': '0.399005', '深圳100': '0.399005',
    '标普500': '100.SPX', 'SPX': '100.SPX', 'spx': '100.SPX', '标普指数': '100.SPX',
    '纳斯达克': '100.NDX', '纳斯达克指数': '100.NDX', 'NSDQ': '100.NDX', 'nsdq': '100.NDX',
    '道琼斯': '100.DJIA', 'DJIA': '100.DJIA', 'dqs': '100.DJIA', '道琼斯指数': '100.DJIA',
    '韩国KOSPI': '100.KS11', '韩国综合': '100.KS11', '韩国综合指数': '100.KS11', '韩国指数': '100.KS11',
    '加拿大S&P/TSX': '100.TSX', '加拿大指数': '100.TSX',
    '巴西BOVESPA': '100.BVSP', '巴西指数': '100.BVSP',
    '墨西哥BOLSA': '100.MXX', '墨西哥指数': '100.MXX',
    '俄罗斯RTS': '100.RTS', '俄罗斯指数': '100.RTS',
}

@retry(tries=3, delay=1)
def get_code_id(code, mode=0):
    """
    生成东方财富股票专用的行情ID
    code:可以是代码或简称或英文
    """
    if code in code_id_dict.keys():
        return code_id_dict[code]
    url = 'https://searchapi.eastmoney.com/api/suggest/get'
    params = (
        ('input', f'{code}'),
        ('type', '14'),
        ('token', 'D43BF722C8E33BDC906FB84D85E326E8'),
    )
    response = session.get(url, params=params).json()
    code_dict = response['QuotationCodeTable']['Data']
    if code_dict:
        code_id = code_dict[0]['QuoteID']
        if mode == 2:
            if code_id.startswith("1."):
                code_id = code_id[2:] + ".SH"
            elif code_id.startswith("0."):
                code_id = code_id[2:] + ".SZ"                      
        return code_id  
    return 0

def trans_num(df, ignore_cols):
    '''df为需要转换数据类型的dataframe
    ignore_cols为dataframe中忽略要转换的列名的list
    如ignore_cols=['代码','名称','所处行业']
    '''
    trans_cols = list(set(df.columns) - set(ignore_cols))
    df[trans_cols] = df[trans_cols].apply(lambda s: pd.to_numeric(s, errors='coerce'))
    return df

#同花顺股票池

def get_current_date():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d")

def get_previous_date(days=30):
    today = datetime.date.today()
    last_month = today - datetime.timedelta(days=days)
    return last_month.strftime("%Y-%m-%d")

def get_recent_workday():
    """
    获取最近的工作日
    """
    today = datetime.date.today()
    if today.weekday() == 5:
        return today - datetime.timedelta(days=1)
    elif today.weekday() == 6:
        return today - datetime.timedelta(days=2)
    else:
        return today

# 获取沪深市场全部股票报告期信息
def report_date():
    """
    获取沪深市场的全部股票报告期信息
    """
    fields = {
        'REPORT_DATE': '报告日期',
        'DATATYPE': '季报名称'
    }
    params = (
        ('type', 'RPT_LICO_FN_CPD_BBBQ'),
        ('sty', ','.join(fields.keys())),
        ('p', '1'),
        ('ps', '2000'),

    )
    url = 'https://datacenter.eastmoney.com/securities/api/data/get'
    response = requests.get(
        url,
        headers=request_header,
        params=params)
    items = jsonpath(response.json(), '$..data[:]')
    if not items:
        pd.DataFrame(columns=fields.values())
    df = pd.DataFrame(items)
    df = df.rename(columns=fields)
    df['报告日期'] = df['报告日期'].apply(lambda x: x.split()[0])
    return df

def latest_trade_date():
    #date=stock_realtime('上证指数')['时间'].values[0][:10].replace("-","")
    #if not date:

    fs = market_dict["上证指数"]
    fields = "f124"
    params = (
        ('pn', '1'),
        ('pz', '1000000'),
        ('po', '1'),
        ('np', '1'),
        ('fltt', '2'),
        ('invt', '2'),
        ('fid', 'f3'),
        ('fs', fs),
        ('fields', fields)
    )
    url = 'http://push2.eastmoney.com/api/qt/clist/get'
    json_response = session.get(url,
                                headers=request_header,
                                params=params).json()
    df = pd.DataFrame(json_response['data']['diff'])
    #print(df)
    date = df["f124"].apply(lambda x: str(datetime.date.fromtimestamp(x)))
    return date.values[0][:10].replace("-","")

def latest_report_date():
    df = report_date()
    return df['报告日期'].iloc[0]


def trans_date(date=None):
    '''将日期格式'20220930'转为'2022-09-30'
    '''
    if date is None:
        return latest_report_date()
    elif "Q" in date:
        q2d = {
            "Q1": "-03-31",
            "Q2": "-06-30",
            "Q3": "-09-30",
            "Q4": "-12-31"
        }
        return date[:4] + q2d[date[4:]]
    elif re.match(r'\d{4}中期', date) is not None:
        return date[:4] + "-06-30"
    elif re.match(r'\d{4}年度', date) is not None:
        return date[:4] + "-12-31"
    elif re.match(r'\d{4}年\d{2}月份', date) is not None:
        return date[:4] + "-" + date[5:7]
    elif re.match(r'\d{4}年第\d{1}季度', date) is not None:
        q2d = {
            "年第1季度": "-03-31",
            "年第2季度": "-06-30",
            "年第3季度": "-09-30",
            "年第4季度": "-12-31",                                    
        }
        return date[:4] + q2d[date[4:]]
    elif date is not None and '-' not in date:
        return '-'.join([date[:4], date[4:6], date[6:]])        
    else:
        return date