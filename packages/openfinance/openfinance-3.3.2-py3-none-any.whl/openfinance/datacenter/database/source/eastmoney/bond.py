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

#############################################################################
####债券bond
# 债券基本信息表头
bond_info_field = {
    'SECURITY_CODE': '债券代码',
    'SECURITY_NAME_ABBR': '债券名称',
    'CONVERT_STOCK_CODE': '正股代码',
    'SECURITY_SHORT_NAME': '正股名称',
    'RATING': '债券评级',
    'PUBLIC_START_DATE': '申购日期',
    'ACTUAL_ISSUE_SCALE': '发行规模(亿)',
    'ONLINE_GENERAL_LWR': '网上发行中签率(%)',
    'LISTING_DATE': '上市日期',
    'EXPIRE_DATE': '到期日期',
    'BOND_EXPIRE': '期限(年)',
    'INTEREST_RATE_EXPLAIN': '利率说明'}


def bond_info_single(code):
    """
    获取单只债券基本信息
    code:债券代码
    """
    columns = bond_info_field
    params = (
        ('reportName', 'RPT_BOND_CB_LIST'),
        ('columns', 'ALL'),
        ('source', 'WEB'),
        ('client', 'WEB'),
        ('filter', f'(SECURITY_CODE="{code}")'),
    )

    url = 'http://datacenter-web.eastmoney.com/api/data/v1/get'
    json_response = requests.get(url,
                                 headers=request_header,
                                 params=params).json()
    if json_response['result'] is None:
        return pd.Series(index=columns.values(), dtype='object')
    items = json_response['result']['data']
    s = pd.Series(items[0]).rename(index=columns)
    s = s[columns.values()]
    return s

def bond_info_all():
    """
    获取全部债券基本信息列表
    """
    page = 1
    dfs = []
    columns = bond_info_field
    while 1:
        params = (
            ('sortColumns', 'PUBLIC_START_DATE'),
            ('sortTypes', '-1'),
            ('pageSize', '500'),
            ('pageNumber', f'{page}'),
            ('reportName', 'RPT_BOND_CB_LIST'),
            ('columns', 'ALL'),
            ('source', 'WEB'),
            ('client', 'WEB'),
        )

        url = 'http://datacenter-web.eastmoney.com/api/data/v1/get'
        json_response = requests.get(url,
                                     headers=request_header,
                                     params=params).json()
        if json_response['result'] is None:
            break
        data = json_response['result']['data']
        df = pd.DataFrame(data).rename(
            columns=columns)[columns.values()]
        dfs.append(df)
        page += 1

    df = pd.concat(dfs, ignore_index=True)
    return df

def bond_info(code_list=None):
    """
    获取单只或多只债券基本信息
    code_list : 债券代码列表
    """
    if code_list is None:
        return bond_info_all()
    if isinstance(code_list, str):
        code_list = [code_list]
    ss = []

    @multitasking.task
    def run(code):
        s = bond_info_single(code)
        ss.append(s)

    for code in code_list:
        run(code)
    multitasking.wait_for_tasks()
    df = pd.DataFrame(ss)
    return df