# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:05:59 2022

"""
import re
import json
import pandas as pd
import requests
import time
import hashlib
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
from tqdm import tqdm
import multitasking
from retry import retry

def parse(date=None):
    if not date:
        date = datetime.now()
        return str(date.year), ("0" + str(date.month))[-2:], ("0" + str(date.day))[-2:]
    dates = date.split("-")
    return dates[0], ("0" + dates[1])[-2:] , ("0" + dates[2])[-2:]

def get_economic(date=None):
    """
        r: Date Source: https://rili.jin10.com/day/2023-12-13
    """    
    year, month, day = parse(date)
    url = f"https://cdn-rili.jin10.com/web_data/{year}/daily/{month}/{day}/economics.json"
    print(url)
    headers = {
        "authority": "cdn-rili.jin10.com",
        "method": "GET",
        "path": "/web_data/{year}/daily/{month}/{day}/economics.json",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cache-control": "max-age=0",
        "cookie": "CALENDAR_FAVOR_INDEX_LIST=%5B%5D; kind_g=%5B%223%22%2C%227%22%5D; trend=1; Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1702369291; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1702369291; x-token=; UM_distinctid=18c5d1df18b13d-0d5304fecfd99d-1f525637-16a7f0-18c5d1df18c189a",
        "if-modified-since": "Tue, 13 Dec 2023 08:25:14 GMT",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = json.loads(response.content.decode("utf-8"))
        return content

def get_event(date=None):
    """
        r: Date Source: https://rili.jin10.com/day/2023-12-13
    """
    year, month, day = parse(date)
    url = f"https://cdn-rili.jin10.com/web_data/{year}/daily/{month}/{day}/event.json"
    headers = {
        "authority": "cdn-rili.jin10.com",
        "method": "GET",
        "path": "/web_data/{year}/daily/{month}/{day}/event.json",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cache-control": "max-age=0",
        "cookie": "CALENDAR_FAVOR_INDEX_LIST=%5B%5D; kind_g=%5B%223%22%2C%227%22%5D; trend=1; Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1702369291; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1702369291; x-token=; UM_distinctid=18c5d1df18b13d-0d5304fecfd99d-1f525637-16a7f0-18c5d1df18c189a",
        "if-modified-since": "Tue, 12 Dec 2023 08:25:14 GMT",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = json.loads(response.content.decode("utf-8"))
        return content  

def get_news():
    url = 'https://flash-api.ushknews.com/get_flash_list_with_channel'
    params = {'channel': ''}  # Add your desired channel value here

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cookie': 'UM_distinctid=18c5df1b4d614a7-023ab5901187be-1f525637-16a7f0-18c5df1b4d714ef; Hm_lvt_b024f76f86f0d29747624c878c07ed94=1702383171; Hm_lpvt_b024f76f86f0d29747624c878c07ed94=1702383381',
        'Origin': 'https://www.ushknews.com',
        'Referer': 'https://www.ushknews.com/',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-App-Id': 'brCYec5s1ova317e',
        'X-Version': '1.0.0'
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        content = json.loads(response.content.decode("utf-8"))
        return content