#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2022/9/29 20:27 
'''

import json
import re
import signal
import requests
import pandas as pd
import numpy as np
import multitasking

from tqdm import tqdm

from jsonpath import jsonpath
from datetime import datetime, timedelta

from openfinance.datacenter.database.source.eastmoney.util import (
    request_header, 
    session, 
    market_num_dict,
    get_code_id, 
    trans_num, 
    trade_detail_dict, 
    latest_report_date,
    market_dict
)

signal.signal(signal.SIGINT, multitasking.killall)


##############################################################################
####基金fund

fund_header = {
    'User-Agent': 'EMProjJijin/6.2.8 (iPhone; iOS 13.6; Scale/2.00)',
    'GTOKEN': '98B423068C1F4DEF9842F82ADF08C5db',
    'clientInfo': 'ttjj-iPhone10,1-iOS-iOS13.6',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'fundmobapi.eastmoney.com',
    'Referer': 'https://mpservice.com/516939c37bdb4ba2b1138c50cf69a2e1/release/pages/FundHistoryNetWorth',
}


# 获取基金单位净值（当前净资产大小）和累计净值（自成立以来的整体收益情况）
def fund_data_single(code):
    """
    根据基金代码和要获取的页码抓取基金净值信息
    code : 6 位基金代码
    """
    # 页码
    pz = 50000
    data = {
        'FCODE': f'{code}',
        'IsShareNet': 'true',
        'MobileKey': '1',
        'appType': 'ttjj',
        'appVersion': '6.2.8',
        'cToken': '1',
        'deviceid': '1',
        'pageIndex': '1',
        'pageSize': f'{pz}',
        'plat': 'Iphone',
        'product': 'EFund',
        'serverVersion': '6.2.8',
        'uToken': '1',
        'userId': '1',
        'version': '6.2.8'
    }
    url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNHisNetList'
    json_response = requests.get(
        url,
        headers=fund_header,
        data=data).json()
    rows = []
    columns = ['日期', '单位净值', '累计净值', '涨跌幅']
    if json_response is None:
        return pd.DataFrame(rows, columns=columns)
    datas = json_response['Datas']
    if len(datas) == 0:
        return pd.DataFrame(rows, columns=columns)
    rows = []
    for stock in datas:
        date = stock['FSRQ']
        rows.append({
            '日期': date,
            '单位净值': stock['DWJZ'],
            '累计净值': stock['LJJZ'],
            '涨跌幅': stock['JZZZL']
        })
    df = pd.DataFrame(rows)
    df.index = pd.to_datetime(df['日期'])
    df['涨跌幅'] = df['涨跌幅'].apply(lambda x: 0 if x == '--' else float(x))
    df = df.iloc[:, 1:].astype('float').sort_index()
    return df


# 获取多只基金的累计净值dataframe
def fund_price(code_list):
    '''code_list输入基金list列表
    如code_list=['180003','340006','159901']
    '''

    @multitasking.task
    def run(code):
        temp = fund_data_single(code)
        data[code] = temp['累计净值']

    data = pd.DataFrame()
    for code in tqdm(code_list):
        run(code)
    multitasking.wait_for_tasks()

    return data


# 获取单只或多只基金的历史净值数据
def fund_data(code_list):
    '''code_list输入股票list列表
    如code_list=['中国平安','贵州茅台','工业富联']
    返回多只股票多期时间的面板数据
    '''
    if isinstance(code_list, str):
        code_list = [code_list]
    data_list = []

    @multitasking.task
    def run(code):
        data = fund_data_single(code)
        data['code'] = code
        data_list.append(data)

    for code in tqdm(code_list):
        run(code)
    multitasking.wait_for_tasks()
    # 转换为dataframe
    df = pd.concat(data_list, axis=0)
    return df

def fund_code(ft=None):
    """
    获取天天基金网公开的全部公墓基金名单
    ft : 'zq': 债券类型基金
        'gp': 股票类型基金
        'etf': ETF 基金
        'hh': 混合型基金
        'zs': 指数型基金
        'fof': FOF 基金
        'qdii': QDII 型基金
        `None` : 全部
    """
    params = [
        ('op', 'dy'),
        ('dt', 'kf'),
        ('rs', ''),
        ('gs', '0'),
        ('sc', 'qjzf'),
        ('st', 'desc'),
        ('es', '0'),
        ('qdii', ''),
        ('pi', '1'),
        ('pn', '50000'),
        ('dx', '0')]

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Accept': '*/*',
        'Referer': 'http://fund.eastmoney.com/data/fundranking.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    if ft is not None:
        params.append(('ft', ft))

    url = 'http://fund.eastmoney.com/data/rankhandler.aspx'
    response = requests.get(
        url,
        headers=headers,
        params=params)

    columns = ['基金代码', '基金简称']
    results = re.findall('"(\d{6}),(.*?),', response.text)
    df = pd.DataFrame(results, columns=columns)
    return df

def fund_position(code, n=1):
    '''code:基金代码，n:获取最近n期数据，n默认为1表示最近一期数据
    '''
    columns = {
        'GPDM': '股票代码',
        'GPJC': '股票简称',
        'JZBL': '持仓占比',
        'PCTNVCHG': '较上期变化',
    }
    df = pd.DataFrame(columns=columns.values())
    dates = fund_dates(code)[:n]
    dfs = []
    for date in dates:
        params = [
            ('FCODE', code),
            ('appType', 'ttjj'),
            ('deviceid', '3EA024C2-7F22-408B-95E4-383D38160FB3'),
            ('plat', 'Iphone'),
            ('product', 'EFund'),
            ('serverVersion', '6.2.8'),
            ('version', '6.2.8'),
        ]
        if date is not None:
            params.append(('DATE', date))
        url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNInverstPosition'
        json_response = requests.get(url,
                                     headers=fund_header,
                                     params=params).json()
        stocks = jsonpath(json_response, '$..fundStocks[:]')
        if not stocks:
            continue
        date = json_response['Expansion']
        _df = pd.DataFrame(stocks)
        _df['公开日期'] = date
        _df.insert(0, '基金代码', code)
        dfs.append(_df)
    fields = ['基金代码'] + list(columns.values()) + ['公开日期']
    if not dfs:
        return pd.DataFrame(columns=fields)
    df = pd.concat(dfs, axis=0, ignore_index=True).rename(
        columns=columns)[fields]
    # 将object类型转为数值型
    ignore_cols = ['基金代码', '股票代码', '股票简称', '公开日期']
    df = trans_num(df, ignore_cols)
    return df


def fund_dates(code):
    """
    获取历史上更新持仓情况的日期列表
    code : 6 位基金代码
    """
    params = (
        ('FCODE', code),
        ('appVersion', '6.3.8'),
        ('deviceid', '3EA024C2-7F22-408B-95E4-383D38160FB3'),
        ('plat', 'Iphone'),
        ('product', 'EFund'),
        ('serverVersion', '6.3.6'),
        ('version', '6.3.8'),
    )
    url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNIVInfoMultiple'
    json_response = requests.get(
        url,
        headers=fund_header,
        params=params).json()
    if json_response['Datas'] is None:
        return []
    return json_response['Datas']

def fund_perfmance(code):
    """
    获取基金阶段涨跌幅度
    code : 6 位基金代码
    """
    params = (
        ('AppVersion', '6.3.8'),
        ('FCODE', code),
        ('MobileKey', '3EA024C2-7F22-408B-95E4-383D38160FB3'),
        ('OSVersion', '14.3'),
        ('deviceid', '3EA024C2-7F22-408B-95E4-383D38160FB3'),
        ('passportid', '3061335960830820'),
        ('plat', 'Iphone'),
        ('product', 'EFund'),
        ('version', '6.3.6'),
    )
    url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNPeriodIncrease'
    json_response = requests.get(
        url,
        headers=fund_header,
        params=params).json()
    columns = {
        'syl': '收益率',
        'avg': '同类平均',
        'rank': '同类排行',
        'sc': '同类总数',
        'title': '时间段'}
    titles = {'Z': '近一周',
              'Y': '近一月',
              '3Y': '近三月',
              '6Y': '近六月',
              '1N': '近一年',
              '2Y': '近两年',
              '3N': '近三年',
              '5N': '近五年',
              'JN': '今年以来',
              'LN': '成立以来'}
    df = pd.DataFrame(json_response['Datas'])
    df = df[list(columns.keys())].rename(columns=columns)
    df['时间段'] = titles.values()
    df.insert(0, '基金代码', code)
    # 将object类型转为数值型
    ignore_cols = ['基金代码', '时间段']
    df = trans_num(df, ignore_cols)
    return df

def fund_base_info(code):
    """
    获取基金的一些基本信息
    code : 6 位基金代码
    """
    params = (
        ('FCODE', code),
        ('deviceid', '3EA024C2-7F22-408B-95E4-383D38160FB3'),
        ('plat', 'Iphone'),
        ('product', 'EFund'),
        ('version', '6.3.8'),
    )
    url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNNBasicInformation'
    json_response = requests.get(
        url,
        headers=fund_header,
        params=params).json()
    columns = {
        'FCODE': '基金代码',
        'SHORTNAME': '基金简称',
        'ESTABDATE': '成立日期',
        'RZDF': '涨跌幅',
        'DWJZ': '最新净值',
        'JJGS': '基金公司',
        'FSRQ': '净值更新日期',
        'COMMENTS': '简介',
    }
    items = json_response['Datas']
    if not items:
        return pd.Series(index=columns.values())

    ss = pd.Series(json_response['Datas']).rename(
        index=columns)[columns.values()]

    ss = ss.apply(lambda x: x.replace('\n', ' ').strip()
                  if isinstance(x, str) else x)
    return ss


def fund_info(code=None, ft='gp'):
    """
    获取基金基本信息
    code:可以输入单只基金代码或多只基金的list
    """
    if code is None:
        code = list(fund_code(ft)['基金代码'])
    if isinstance(code, str):
        code = [code]
    ss = []

    @multitasking.task
    def start(code):
        s = fund_base_info(code)
        ss.append(s)
        pbar.update()

    pbar = tqdm(total=len(code))
    for c in code:
        start(c)
    multitasking.wait_for_tasks()
    df = pd.DataFrame(ss)
    return df