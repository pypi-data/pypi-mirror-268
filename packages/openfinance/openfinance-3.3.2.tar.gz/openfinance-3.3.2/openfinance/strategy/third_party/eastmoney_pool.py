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
    market_dict,
    latest_trade_date    
)
from openfinance.datacenter.knowledge.decorator import register

signal.signal(signal.SIGINT, multitasking.killall)

#实时交易盘口异动数据
def realtime_change(flag=None):
    '''
    flag：盘口异动类型，默认输出全部类型的异动情况
    可选：['火箭发射', '快速反弹','加速下跌', '高台跳水', '大笔买入', '大笔卖出', 
        '封涨停板','封跌停板', '打开跌停板','打开涨停板','有大买盘','有大卖盘', 
        '竞价上涨', '竞价下跌','高开5日线','低开5日线',  '向上缺口','向下缺口', 
        '60日新高','60日新低','60日大幅上涨', '60日大幅下跌']
    '''
    #默认输出市场全部类型的盘口异动情况（相当于短线精灵）
    changes_list=['火箭发射', '快速反弹','加速下跌', '高台跳水', '大笔买入', 
        '大笔卖出', '封涨停板','封跌停板', '打开跌停板','打开涨停板','有大买盘',
        '有大卖盘', '竞价上涨', '竞价下跌','高开5日线','低开5日线', '向上缺口',
        '向下缺口', '60日新高','60日新低','60日大幅上涨', '60日大幅下跌']
    n=range(1,len(changes_list)+1)
    change_dict=dict(zip(n,changes_list))
    if flag is not None:
        if isinstance(flag,int):
            flag=change_dict[flag]
        return stock_changes(symbol=flag)
    else:
        
        df=stock_changes(symbol=changes_list[0])
        for s in changes_list[1:]:
            temp=stock_changes(symbol=s)
            df=pd.concat([df,temp])
            df=df.sort_values('时间',ascending=False)
        return df

#东方财富网实时交易盘口异动数据
def stock_changes(symbol):
    """
    东方财富行盘口异动
    http://quote.eastmoney.com/changes/
    :symbol:  {'火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', 
               '有大买盘', '竞价上涨', '高开5日线', '向上缺口', '60日新高', 
               '60日大幅上涨', '加速下跌', '高台跳水', '大笔卖出', '封跌停板', 
               '打开涨停板', '有大卖盘', '竞价下跌', '低开5日线', '向下缺口', 
               '60日新低', '60日大幅下跌'}
    """
    url = "http://push2ex.eastmoney.com/getAllStockChanges"
    symbol_map = {
        "火箭发射": "8201",
        "快速反弹": "8202",
        "大笔买入": "8193",
        "封涨停板": "4",
        "打开跌停板": "32",
        "有大买盘": "64",
        "竞价上涨": "8207",
        "高开5日线": "8209",
        "向上缺口": "8211",
        "60日新高": "8213",
        "60日大幅上涨": "8215",
        "加速下跌": "8204",
        "高台跳水": "8203",
        "大笔卖出": "8194",
        "封跌停板": "8",
        "打开涨停板": "16",
        "有大卖盘": "128",
        "竞价下跌": "8208",
        "低开5日线": "8210",
        "向下缺口": "8212",
        "60日新低": "8214",
        "60日大幅下跌": "8216",
    }
    reversed_symbol_map = {v: k for k, v in symbol_map.items()}
    params = {
        "type": symbol_map[symbol],
        "pageindex": "0",
        "pagesize": "5000",
        "ut": "7eea3edcaed734bea9cbfc24409ed989",
        "dpt": "wzchanges",
        "_": "1624005264245",
    }
    res = requests.get(url, params=params)
    data_json = res.json()
    df = pd.DataFrame(data_json["data"]["allstock"])
    df["tm"] = pd.to_datetime(df["tm"], format="%H%M%S").dt.time
    df.columns = ["时间","代码","_","名称","板块","相关信息",]
    df= df[["时间","代码","名称","板块","相关信息",]]
    df["板块"] = df["板块"].astype(str)
    df["板块"] = df["板块"].map(reversed_symbol_map)
    return df

@register(name="涨停的股票", description="Get stocks at uptick limit", graph_node=False)
def get_uptick_limit_stock(date= None) :
    """## chinese: 查询涨停的股票|涨停股票
    ## english: Get stocks at uptick limit
    ## args: 
        date:日期
    ## extra:
    """
    try:
        date=latest_trade_date()
        url = 'http://push2ex.eastmoney.com/getTopicZTPool'
        params = {
            'ut': '7eea3edcaed734bea9cbfc24409ed989',
            'dpt': 'wz.ztzt',
            'Pageindex': '0',
            'pagesize': '10',
            'sort': 'fbt:asc',
            'date': date,
            '_': '1621590489736',
        }
        #print(params)
        r = requests.get(url, params=params)
        data_json = r.json()
        if data_json['data'] is None:
            return EMPTY_DATA
        temp_df = pd.DataFrame(data_json['data']['pool'])
        temp_df.reset_index(inplace=True)
        temp_df['index'] = range(1, len(temp_df)+1)
        old_cols=['序号','代码','_','名称','最新价','涨跌幅','成交额(百万)','流通市值(百万)',
            '总市值(百万)', '换手率','连板数','首次封板时间','最后封板时间',
            '封板资金(百万)','炸板次数','所属行业','涨停统计',]
        temp_df.columns =  old_cols
        temp_df['涨停统计'] = (temp_df['涨停统计'].apply(lambda x: dict(x)['days']
                    ).astype(str) + "/" + temp_df['涨停统计']
                .apply(lambda x: dict(x)['ct']).astype(str))
        new_cols=['代码','名称','涨跌幅','最新价','换手率','成交额(百万)','流通市值(百万)',
            '总市值(百万)','封板资金(百万)','首次封板时间','最后封板时间','炸板次数',
            '涨停统计','连板数','所属行业',]
        df = temp_df[new_cols].copy()
        df['首次封板时间'] = df['首次封板时间'].apply(lambda s:str(s)[-6:-4]+':'+str(s)[-4:-2])
        df['最后封板时间'] = df['最后封板时间'].apply(lambda s:str(s)[-6:-4]+':'+str(s)[-4:-2])
        df['最新价'] = df['最新价'] / 1000
    
        # 将object类型转为数值型
        ignore_cols = ['代码','名称','最新价','首次封板时间','最后封板时间','涨停统计','所属行业',]
        df = trans_num(df, ignore_cols)
        df[['成交额(百万)','流通市值(百万)','总市值(百万)','封板资金(百万)']]=(df[['成交额(百万)',
            '流通市值(百万)','总市值(百万)','封板资金(百万)']]/1000000)
        return df.round(3).to_string()
    except:
        return EMPTY_DATA

@register(name="跌停股的股票", description="Get stocks at downtick limit", graph_node=False)
def get_downtick_limit_stock(date = None):
    """## chinese: 查询跌停股的股票|跌停股票
    ## english: Get stocks at downtick limit
    ## args: 
        date:日期
    ## extra: http://quote.eastmoney.com/ztb/detail#type=dtgc
    """
    try:
        date=latest_trade_date()
        url = 'http://push2ex.eastmoney.com/getTopicDTPool'
        params = {
            'ut': '7eea3edcaed734bea9cbfc24409ed989',
            'dpt': 'wz.ztzt',
            'Pageindex': '0',
            'pagesize': '10000',
            'sort': 'fund:asc',
            'date': date,
            '_': '1621590489736',
        }
        res = requests.get(url, params=params)
        data_json = res.json()
        if data_json['data'] is None:
            return EMPTY_DATA
        temp_df = pd.DataFrame(data_json['data']['pool'])
        temp_df.reset_index(inplace=True)
        temp_df['index'] = range(1, len(temp_df)+1)
        old_cols=['序号','代码','_','名称','最新价','涨跌幅','成交额(百万)','流通市值(百万)',
            '总市值(百万)','动态市盈率','换手率','封板资金(百万)','最后封板时间','板上成交额',
            '连续跌停','开板次数','所属行业',]
        temp_df.columns = old_cols
        new_cols=['代码','名称','涨跌幅','最新价','换手率','最后封板时间',
            '连续跌停','开板次数','所属行业','成交额(百万)','封板资金(百万)','流通市值(百万)',
            '总市值(百万)']
        df = temp_df[new_cols].copy()
        df['最新价'] = df['最新价'] / 1000
        df['最后封板时间'] = df['最后封板时间'].apply(lambda s:str(s)[-6:-4]+':'+str(s)[-4:-2])
        # 将object类型转为数值型
        ignore_cols = ['代码','名称','最新价','最后封板时间','所属行业',]
        df = trans_num(df, ignore_cols)
        df[['成交额(百万)','流通市值(百万)','总市值(百万)','封板资金(百万)']]=(df[['成交额(百万)',
            '流通市值(百万)','总市值(百万)','封板资金(百万)']]/1000000)
        return df.round(3).to_string()
    except:
        return EMPTY_DATA

@register(name="强势股票", description="Get stocks with strong upward trends", graph_node=False)
def get_strong_momentum_stock(date= None):
    """## chinese: 查询强势股的股票|强势股票
    ## english: Get stocks with strong upward trends
    ## args: 
        date:日期
    ## extra:
    """
    try:
        date=latest_trade_date()
        print(date)
        url = 'http://push2ex.eastmoney.com/getTopicQSPool'
        params = {
            'ut': '7eea3edcaed734bea9cbfc24409ed989',
            'dpt': 'wz.ztzt',
            'Pageindex': '0',
            'pagesize': '10',
            'sort': 'zdp:desc',
            'date': date,
            '_': '1621590489736',
        }
        res = requests.get(url, params=params)
        data_json = res.json()

        if data_json['data'] is None:
            return EMPTY_DATA
        temp_df = pd.DataFrame(data_json['data']['pool'])
        temp_df.reset_index(inplace=True)
        temp_df['index'] = range(1, len(temp_df)+1)
        old_cols=['序号','代码','_','名称','最新价','涨停价','_','涨跌幅',
            '成交额(百万)','流通市值(百万)','总市值(百万)', '换手率','是否新高','入选理由',
            '量比','涨速','涨停统计','所属行业',]
        temp_df.columns = old_cols
        temp_df['涨停统计'] = temp_df['涨停统计'].apply(lambda x: dict(x)['days']).astype(str) + "/" + temp_df['涨停统计'].apply(lambda x: dict(x)['ct']).astype(str)
        new_cols=['代码','名称','涨跌幅','最新价','涨停价','换手率','涨速','是否新高','量比',
                '涨停统计','入选理由','所属行业','成交额(百万)','流通市值(百万)','总市值(百万)', ]
        df = temp_df[new_cols].copy()
        df[['最新价','涨停价']] = df[['最新价','涨停价']] / 1000
        df[['成交额(百万)','流通市值(百万)','总市值(百万)']]=(df[['成交额(百万)',
            '流通市值(百万)','总市值(百万)']]/1000000)
        rr={1: '60日新高', 2: '近期多次涨停', 3: '60日新高且近期多次涨停'}
        df['入选理由']=df['入选理由'].apply(lambda s: rr[s])
        return df.round(2).to_string()
    except:
        return EMPTY_DATA