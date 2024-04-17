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

def industry_money_flow(code):
    """## chinese: 获取行业的10日资金流
    ## english: Get institutional money flow of industry|industry money flow
    ## args:
        code: 股票名称
    ## https://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112306983464741861547_1694936948617&fid=f174&po=1&pz=100&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A90+t%3A2&fields=f12%2Cf14%2Cf2%2Cf160%2Cf174%2Cf175%2Cf176%2Cf177%2Cf178%2Cf179%2Cf180%2Cf181%2Cf182%2Cf183%2Cf260%2Cf261%2Cf124%2Cf1%2Cf13
    """
    try:

        code = code.strip()
        industry_info_dict = {
            'f12': 'code',
            'f14': 'industry_name',
            'f160': '10 days percentage change (%)',
            'f174': '10 days money flow (元)',
            'f175': '10 dyas money flow percentage (%)'
        }
        code_id = get_code_id(code)

        # todo 代码规范待确认
        if "90" in code_id:
            code_id = code_id[3:]
        else:
            return EMPTY_DATA
        fields = ",".join(industry_info_dict.keys())
        params = {
            'fid': 'f174',
            'po': '1',
            'pz': '100',
            'pn': '1',
            'np': '1',
            'fltt': '2',
            'invt': '2',
            'fs': 'm:90+t:2',
            'fields': fields,
        }

        url = "http://push2.eastmoney.com/api/qt/clist/get"
        res = requests.get(url, params=params)
        result = ""
        res = json.loads(res.text)
        res_num = res.get('data', {}).get('total', 0)
        if res_num > 0:
            res_list = res.get('data', {}).get('diff', [])
            for item in res_list:
                code = item.get('f12', '')
                code_name = item.get('f14', '')
                money_flow = item.get('f174', '')
                money_flow_percentage = item.get('f175', '')
                percentage_change = item.get('f160', '')
                if code == code_id:
                    result += f"{code_name}, 10日资金流入{money_flow}元, 10日资金流占比{money_flow_percentage}%, 10日涨跌幅: {percentage_change}%\n"
                    break
        if result == "":
            return EMPTY_DATA
        return result
    except:
        return EMPTY_DATA

def industry_valuation(code):
    """## chinese: 获取行业的估值
    ## english: Get institutional valuation of industry|industry valuation
    ## args:
        code: 股票名称
    ## https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery112308402197609827453_1694942480056&reportName=RPT_VALUEINDUSTRY_DET&columns=ALL&quoteColumns=&pageNumber=1&sortColumns=PE_TTM&sortTypes=1&source=WEB&client=WEB&filter=(TRADE_DATE%3D%272023-09-15%27)(PE_TTM%3E0)&_=1694942480058
    """
    try:
        #print(code)    
        code = code.strip()
        code_id = get_code_id(code)
        #print(code_id)
        # todo 代码规范待确认
        if "90" in code_id:
            code_id = code_id[3:]
        else:
            return EMPTY_DATA
        params = {
            'reportName': 'RPT_VALUEINDUSTRY_DET',
            'columns': 'ALL',
            'pageNumber': '1',
            'sortColumns': 'PE_TTM',
            'sortTypes': '1',
            'source': 'WEB',
            'client': 'WEB',
            'filter': f'(TRADE_DATE=\'{get_recent_workday()}\')(PE_TTM>0)',
            '_': '1694942480058'
        }

        url = "http://datacenter-web.eastmoney.com/api/data/v1/get"
        print(params)
        res = requests.get(url, params=params)
        result = ""
        res = json.loads(res.text)
        print(res)
        res_list = res.get('result', {}).get('data', [])
        for i in range(2, 10):
            params.update({'pageNumber': str(i)})
            res = requests.get(url, params=params)
            res = json.loads(res.text)
            res_tmp = res.get('result', {})
            if not res_tmp:
                break
            res_tmp = res.get('result', {}).get('data', [])
            res_list.extend(res_tmp)

        if res_list:
            for item in res_list:
                code_name = item.get('BOARD_NAME', '')
                PE_TTM = item.get('PE_TTM', '')  # 滚动市盈率
                PE_LAR = item.get('PE_LAR', '')  # 静态市盈率
                PB_MRQ = item.get('PB_MRQ', '')  # 市净率
                PCF_OCF_TTM = item.get('PCF_OCF_TTM', '')  # 市现率
                PEG_CAR = item.get('PEG_CAR', '')  # peg
                PS_TTM = item.get('PS_TTM', '')  # 市销率
                MARKET_CAP_VAG = item.get('MARKET_CAP_VAG', '')  # 行业平均市值

                if code_name == code:
                    result += f"{code_name}, 滚动市盈率: {PE_TTM}, 静态市盈率: {PE_LAR}, 市净率: {PB_MRQ}, PEG: {PEG_CAR}, 行业平均市值: {MARKET_CAP_VAG}\n"
                    break
        if result == "":
            return EMPTY_DATA
        return result
    except:
        return EMPTY_DATA        

### 东方财富 行业###
def get_industry_by_company(code):
    """## chinese: 给定公司的行业发展信息
    ## english: Get Industry Analysis given company
    ## args:
        code: 股票名称
    ## 
    """
    try:
        code = code.strip()
        code_id = get_code_id(code)
        url = "http://push2.eastmoney.com/api/qt/slist/get"
        params = {
            "fltt": 1,
            "invt": 2,
            "secid": code_id,
            "ut": "fa5fd1943c7b386f172d6893dbfba10b",
            "pi": 0,
            "po": 1,
            "np": 1,
            "pz": 5,
            "spt": 3,
            "wbp2u": "|0|0|0|web",
            "fields": "f14,f12",
            "_": 1687091239523,
        }
        res = requests.get(url, params=params)
        #print(res.text, code_id, get_previous_month_date(), get_current_date())
        res = json.loads(res.text)
        art_list = res['data']['diff']
        #for i in art_list:
        #    result += i["f14"] + " " + i["f12"] +"\n"
        #return result
        #print(art_list)
        return art_list[0]["f12"][2:]
    except:
        return EMPTY_DATA
    

def industry_index_trend(code):
    """## chinese: 获取行业指数趋势
    ## english: Get institutional index trend
    ## args:
        code: 股票名称
    ## https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123045720624426005796_1697901296839&reportName=RPT_INDUSTRY_INDEX&columns=REPORT_DATE%2CINDICATOR_VALUE%2CCHANGE_RATE%2CCHANGERATE_3M%2CCHANGERATE_6M%2CCHANGERATE_1Y%2CCHANGERATE_2Y%2CCHANGERATE_3Y%2CIS_NEWEST%2CBOARD_CODE%2CBOARD_NAME%2CCONCEPT_CODE%2CCONCEPT_NAME%2CINDICATOR_ID%2CINDICATOR_NAME%2CRANK_LABEL&filter=(IS_NEWEST%3D%22True%22)&pageSize=1000&source=WEB&client=WEB&_=1697901296841

    """

    # try:
    code = code.strip()
    code_id = get_code_id(code)
    # todo 代码规范待确认
    # if "90" in code_id:
    #     code_id = code_id[3:]
    # else:
    #     return EMPTY_DATA
    params = {
        'reportName': 'RPT_INDUSTRY_INDEX',
        'columns': 'REPORT_DATE,INDICATOR_VALUE,CHANGE_RATE,CHANGERATE_3M,CHANGERATE_6M,CHANGERATE_1Y,CHANGERATE_2Y,CHANGERATE_3Y,IS_NEWEST,BOARD_CODE,BOARD_NAME,CONCEPT_CODE,CONCEPT_NAME,INDICATOR_ID,INDICATOR_NAME,RANK_LABEL',
        'pageSize': '1000',
        'client': 'WEB',
        'source': 'WEB',
        'filter': f'(IS_NEWEST=\"True\")',
        '_': '1697901296841'
    }

    url = "http://datacenter-web.eastmoney.com/api/data/v1/get"
    res = requests.get(url, params=params)
    # print(res.url)

    result = ""
    res = json.loads(res.text)
    res_list = res.get('result', {}).get('data', [])

    if res_list:
        deduplicate_keys = set()
        for item in res_list:
            code_name = item.get('BOARD_NAME', '')
            CHANGERATE_3M = item.get('CHANGERATE_3M', '')  # 指标近3月变化率
            CHANGERATE_6M = item.get('CHANGERATE_6M', '')
            CHANGERATE_1Y = item.get('CHANGERATE_1Y', '')
            CHANGERATE_2Y = item.get('CHANGERATE_2Y', '')
            CHANGERATE_3Y = item.get('CHANGERATE_3Y', '')
            INDICATOR_NAME = item.get('INDICATOR_NAME', '')  # 行业下细分指数名称

            if code_name in code or code in code_name:
                if INDICATOR_NAME not in deduplicate_keys:
                    result += f"{INDICATOR_NAME}的近3个月变化率: {CHANGERATE_3M}; {INDICATOR_NAME}的近6个月变化率: {CHANGERATE_6M}; {INDICATOR_NAME}的近1年变化率: {CHANGERATE_1Y}\n"
                    deduplicate_keys.add(INDICATOR_NAME)

    if result == "":
        return EMPTY_DATA
    return result
    # except:
    #     return EMPTY_DATA