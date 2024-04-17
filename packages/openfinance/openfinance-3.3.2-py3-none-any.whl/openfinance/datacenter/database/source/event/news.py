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

def news_cls(date=None, duration=300):
    """
    金十数据-市场快讯
    https://www.jin10.com/
    date: 日期
    """
    """## chinese: 查询市场快讯|市场有哪些新闻
    ## english: Get news of market
    ## args: 
        date: 时间
    ## extra:
    https://www.cls.cn/nodeapi/updateTelegraphList?app=CailianpressWeb&category=&hasFirstVipArticle=1&lastTime=1688630185&os=web&rn=20&subscribedColumnIds=&sv=7.7.5&sign=27f53d3fba6bc9b5b0667d354efa2d8d
    """
    date = int(time.time()) - duration
    url = "https://www.cls.cn/nodeapi/updateTelegraphList"
    params = {
        "app": "CailianpressWeb",
        "hasFirstVipArticle": "1",
        "lastTime": date,
        "rn": 20,
        "sv": "7.7.5",
        "sign": "27f53d3fba6bc9b5b0667d354efa2d8d",
    }
    headers = {
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Content-Type": "application/json;charset=utf-8",
        "Connection": "keep-alive",
        "Host": "www.cls.cn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    data = requests.get(url, params=params, headers=headers).json()
    #ret = ""
    #print(data)
    ret = []
    for d in data['data']['roll_data']:
        t = d['content']
        stock_name = ""
        for s in d['stock_list']:
            stock_name = s['name']
            #ret.append((stock_name, t))
            #ret += stock_name + "\t"
        #ret += t + "\n"
        ret.append((stock_name, t))
    return ret

def get_news_cctv(date= None):
    """
    新闻联播文字稿
    https://tv.cctv.com/lm/xwlb/?spm=C52056131267.P4y8I53JvSWE.0.0
    date: 需要获取数据的日期
    """
    
    now=datetime.now()
    now_date=now.strftime('%Y%m%d')
    if date is None:
        date=now_date
    else:
        date=''.join(date.split('-'))
    if  date>=now_date:
        date=(now-timedelta(1)).strftime('%Y%m%d')
       
    url = f"http://cctv.cntv.cn/lm/xinwenlianbo/{date}.shtml"
    res = requests.get(url)
    title_list = []
    content_list = []
    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Cookie": "cna=DLYSGBDthG4CAbRVCNxSxGT6",
            "Host": "tv.cctv.com",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    }
    if int(date) <= int("20130708"):
        res.encoding = "gbk"
        raw_list = re.findall(r"title_array_01\((.*)", res.text)
        page_url = [
            re.findall("(http.*)", item)[0].split("'")[0]
            for item in raw_list[1:]]   

    elif int(date) < int("20160203"):
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "lxml")
        page_url = [
            item.find("a")["href"]
            for item in soup.find(
                "div", attrs={"id": "contentELMT1368521805488378"}
            ).find_all("li")[1:]]

    else:
        url = f"https://tv.cctv.com/lm/xwlb/day/{date}.shtml"
        res = requests.get(url)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "lxml")
        page_url = [item.find("a")["href"] for item in soup.find_all("li")[1:]]
        
    for page in tqdm(page_url, leave=False):
        try:
            r = requests.get(page, headers=headers)
            r.encoding = "utf-8"
            soup = BeautifulSoup(r.text, "lxml")
            if soup.find("h3"):
                title = soup.find("h3").text
            else:
                title = soup.find("div", attrs={"class": "tit"}).text
            if soup.find("div", attrs={"class": "cnt_bd"}):
                content = soup.find("div", attrs={"class": "cnt_bd"}).text
            else:
                content = soup.find(
                    "div", attrs={"class": "content_area"}
                    ).text
            title_list.append(
                    title.strip("[视频]").strip().replace("\n", " ")
                )
            content_list.append(
                    content.strip()
                    .strip("央视网消息(新闻联播)：")
                    .strip("央视网消息（新闻联播）：")
                    .strip("(新闻联播)：")
                    .strip()
                    .replace("\n", " ")
                )
        except:
            continue
    df = pd.DataFrame(
            [[date] * len(title_list), title_list, content_list],
            index=["date", "title", "content"],
        ).T
    return df

def get_dates(start=None,end=None):
    if start is None:
        start=(datetime.now()).strftime('%Y%m%d')
    if end is None:
        end=(datetime.now()).strftime('%Y%m%d')
    if start>end:
        start=end
    dates=pd.date_range(start,end)
    dates=[s.strftime('%Y%m%d') for s in dates]
    return dates

def news_cctv(start=None,end=None):
    '''获取某日期期间的所有新闻联播数据
    start:起始日期，如'20220930'
    end:结束日期，如'20221001'
    '''
    dates=get_dates(start,end)
    data_list=[]
    @multitasking.task
    @retry(tries=3, delay=1)
    def run(date):
        data = get_news_cctv(date)
        data_list.append(data)

    for date in tqdm(dates):
        run(date)
    multitasking.wait_for_tasks()
    # 转换为dataframe
    df = pd.concat(data_list, axis=0,ignore_index=True)
    return df

def news_js(start,end):
    '''获取某日期期间的所有金十数据-市场快讯数据
    start:起始日期，如'20220930'
    end:结束日期，如'20221001'
    '''
    dates=get_dates(start,end)
    data_list=[]
    @multitasking.task
    @retry(tries=3, delay=1)
    def run(date):
        data = get_js_news(date)
        data_list.append(data)

    for date in tqdm(dates):
        run(date)
    multitasking.wait_for_tasks()
    # 转换为dataframe
    df = pd.concat(data_list, axis=0,ignore_index=True)
    return df