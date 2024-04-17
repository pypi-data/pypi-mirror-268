# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:53:48 2022

"""
import pandas as pd
import requests
import calendar
import json
from typing import Any
from datetime import datetime
from jsonpath import jsonpath
from tqdm import tqdm
from bs4 import BeautifulSoup
from openfinance.datacenter.database import EMPTY_DATA
from openfinance.datacenter.database.source.eastmoney.util import (
    latest_report_date,
    trans_num,
    get_code_id,
    request_header,
    session,
    get_current_date,
    get_previous_date,
    get_recent_workday
)

def stock_holder_top10(code, n=1):
    """## chinese: 获取公司前十大股东|股东成分
    ## english: Get Top10 stakeholder of company|company shareholder
    ## args:
        code: 股票名称
    ##
    """
    try:
        code = code.strip()
        code_id = get_code_id(code)
        fields = {
            'GuDongDaiMa': '股东代码',
            'GuDongMingCheng': '股东名称',
            'ChiGuShu': '持股数(亿)',
            'ChiGuBiLi': '持股比例(%)',
            'ZengJian': '增减',
            'BianDongBiLi': '变动率(%)'}
        mk = code_id.split('.')[0]
        stock_code = code_id.split('.')[1]
        fc = f'{stock_code}02' if mk == '0' else f'{stock_code}01'
        data0 = {"fc": fc}
        url0 = 'https://emh5.eastmoney.com/api/GuBenGuDong/GetFirstRequest2Data'
        res = requests.post(url0, json=data0).json()
        dates = jsonpath(res, '$..BaoGaoQi')
        df_list = []

        for date in dates[:n]:
            data = {"fc": fc, "BaoGaoQi": date}
            url = 'https://emh5.eastmoney.com/api/GuBenGuDong/GetShiDaLiuTongGuDong'
            response = requests.post(url, json=data)
            response.encoding = 'utf-8'
            items = jsonpath(
                response.json(), '$..ShiDaLiuTongGuDongList[:]')
            if not items:
                continue
            df = pd.DataFrame(items)
            df.rename(columns=fields, inplace=True)
            df.insert(0, '代码', [stock_code for _ in range(len(df))])
            df.insert(1, '日期', [date for _ in range(len(df))])
            del df['IsLink']
            del df['股东代码']
            df_list.append(df)

        dff = pd.concat(df_list, axis=0, ignore_index=True)
        # 将object类型转为float
        trans_cols = ['持股数(亿)', '持股比例(%)', '变动率(%)']
        for col in trans_cols:
            dff[col] = dff[col].apply(lambda x: float(x[:-1]) if x[-1] in ['亿', '%'] else 0)
        return dff
    except:
        return EMPTY_DATA

def get_company_valuation(code="贵州茅台", **kwargs: Any):
    """## chinese: 获取公司估值情况|公司估值
    ## english: Get stock valuation by company|stock valuation
    ## args:
        code: 股票名称
    ## extra: 
    """
    try:
        stock_info_dict = {
            'f163': 'Price/Earning Ratio',
            'f164': 'TTM Price/Earning Ratio',
            'f167': 'P/B Ratio'
        }
        code_id = get_code_id(code)
        fields = ",".join(stock_info_dict.keys())
        params = (
            ('ut', 'fa5fd1943c7b386f172d6893dbfba10b'),
            ('invt', '2'),
            ('fltt', '2'),
            ('fields', fields),
            ('secid', code_id)
        )
        url = 'http://push2.eastmoney.com/api/qt/stock/get'
        json_response = session.get(url,
                                    headers=request_header,
                                    params=params).json()
        items = json_response['data']
        if not items:
            return EMPTY_DATA

        s = pd.Series(items, dtype='object').rename(
            index=stock_info_dict)
        return s.to_string()
    except:
        return EMPTY_DATA
