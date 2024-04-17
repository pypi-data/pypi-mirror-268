# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:53:48 2022

"""
import pandas as pd
import requests
import json
from typing import Any
from datetime import datetime
from jsonpath import jsonpath
from tqdm import tqdm
from bs4 import BeautifulSoup
from openfinance.datacenter.database import EMPTY_DATA
from openfinance.datacenter.database.source.eastmoney.industry import (
    get_industry_by_company
)
from openfinance.datacenter.database.source.eastmoney.util import (
    trans_num,
    get_code_id,
    get_current_date,
    get_previous_date,
    get_recent_workday
)

def industry_institutional_rating(code):
    """## chinese: 获取行业的机构评级|行业评级
    ## english: Get institutional rating of industry|industry institutional rating
    ## args:
        code: 股票名称
    ## http://reportapi.eastmoney.com/report/list?cb=callback7187406&beginTime=2021-06-18&endTime=2023-06-18&pageNo=1&pageSize=5&qType=1&industryCode=1029&fields=orgCode%2CorgSName%2CemRatingName%2CencodeUrl%2Ctitle%2CpublishDate&_=1687091682364
    """
    try:
        code = code.strip()
        url = "http://reportapi.eastmoney.com/report/list"
        params = {
            "beginTime": get_previous_date(30),
            "endTime": get_current_date(),
            "pageNo": 1,
            "qType": 1,
            "pageSize": 2,
            "industryCode": code,
            "fields": "orgSName,emRatingName,title",
            "_": 1687091239523,
        }
        res = requests.get(url, params=params)
        #print(res.text, code_id, get_previous_date(30), get_current_date())
        result = ""
        res = json.loads(res.text)
        art_list = res['data']
        for i in art_list:
            result += i["orgSName"] + " " + i["emRatingName"] + " " + i["title"] + "\n"
        return result
    except:
        return EMPTY_DATA

# need to improve for single company
def stock_institutional_rating(code, **kwargs: Any):
    """## chinese: 获取公司的机构评级|机构评级
    ## english: get institutional rating of company|company institutional rating
    ## args:
        code: 股票名称
    ## 
    """
    try:
        code = code.strip()
        code_id = get_code_id(code)[2:]
        url = "http://reportapi.eastmoney.com/report/list"
        params = {
            "beginTime": get_previous_date(30),
            "endTime": get_current_date(),
            "pageNo": 1,
            "qType": 1,
            "pageSize": 2,
            "code": code_id,
            "fields": "orgSName,emRatingName,title",
            "_": 1687091239523,
        }
        res = requests.get(url, params=params)
        #print(res.text, code_id, get_previous_date(30), get_current_date())
        result = ""
        res = json.loads(res.text)
        art_list = res['data']
        if len(art_list):
            for i in art_list:
                result += i["orgSName"] + " " + i["emRatingName"] + " " + i["title"] + "\n"
        else:
            industryCode = get_industry_by_company(code)
            return industry_institutional_rating(industryCode)
        return result
    except:
        return EMPTY_DATA

def get_company_news(name):
    try:
        name = name.strip()
        code_id = get_code_id(name)
        url = "http://np-listapi.eastmoney.com/comm/web/getListInfo"
        params = {
            "cfh": 1,
            "client": "web",
            "mTypeAndCode": code_id,
            "type": 1,
            "pageSize": 5,
            "traceId": 479298450,
            "_": 1687091239523
        }
        res = requests.get(url, params=params)
        # print(res.text)
        result = ""
        res = json.loads(res.text)
        if res['message'] == "success":
            art_list = res['data']['list']
            for i in art_list:
                result += i["Art_Title"] + "\n"
        return result
    except:
        return EMPTY_DATA 