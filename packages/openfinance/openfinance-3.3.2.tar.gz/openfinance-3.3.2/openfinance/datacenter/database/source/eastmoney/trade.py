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

signal.signal(signal.SIGINT, multitasking.killall)

# 获取某指定市场所有标的最新行情指标
def market_realtime(market='沪深A'):
    """
    获取沪深市场最新行情总体情况（涨跌幅、换手率等信息）
     market表示行情名称或列表，默认沪深A股
    '沪深京A':沪深京A股市场行情; '沪深A':沪深A股市场行情;'沪A':沪市A股市场行情
    '深A':深市A股市场行情;北A :北证A股市场行情;'可转债':沪深可转债市场行情;
    '期货':期货市场行情;'创业板':创业板市场行情;'美股':美股市场行情;
    '港股':港股市场行情;'中概股':中国概念股市场行情;'新股':沪深新股市场行情;
    '科创板':科创板市场行情;'沪股通' 沪股通市场行情;'深股通':深股通市场行情;
    '行业板块':行业板块市场行情;'概念板块':概念板块市场行情;
    '沪深指数':沪深系列指数市场行情;'上证指数':上证系列指数市场行情
    '深证指数':深证系列指数市场行情;'ETF' ETF基金市场行情;'LOF' LOF 基金市场行情
    """
    fs = market_dict[market]

    fields = ",".join(trade_detail_dict.keys())
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
    df = df.rename(columns=trade_detail_dict)
    df = df[trade_detail_dict.values()]
    df['ID'] = df['编号'].astype(str) + '.' + df['代码'].astype(str)
    df['市场'] = df['编号'].astype(str).apply(
        lambda x: market_num_dict.get(x))
    df['时间'] = df['更新时间戳'].apply(lambda x: str(datetime.fromtimestamp(x)))
    del df['更新时间戳']
    del df['编号']
    del df['ID']
    del df['市场']
    # 将object类型转为数值型
    ignore_cols = ['代码', '名称', '时间']
    df = trans_num(df, ignore_cols)
    return df


# 获取单个或多个证券的最新行情指标
def stock_realtime(code_list):
    """
    获取股票、期货、债券的最新行情指标
    code_list:输入单个或多个证券的list
    """
    if isinstance(code_list, str):
        code_list = [code_list]
    # print(code_list)
    code_ids = [get_code_id(code)
            for code in code_list]
    fields = ",".join(trade_detail_dict.keys())
    url = 'https://push2.eastmoney.com/api/qt/ulist.np/get'
    DIV = 5
    step = int((len(code_ids) + DIV - 1)/DIV)

    def inner(secids):
        params = (
            ('OSVersion', '14.3'),
            ('appVersion', '6.3.8'),
            ('fields', fields),
            ('fltt', '2'),
            ('plat', 'Iphone'),
            ('product', 'EFund'),
            ('secids', ",".join(secids)),
            ('serverVersion', '6.3.6'),
            ('version', '6.3.8'),
        )
        
        json_response = session.get(url,
                                    headers=request_header,
                                    params=params).json()
        rows = jsonpath(json_response, '$..diff[:]')
        if not rows:
            df = pd.DataFrame(columns=trade_detail_dict.values())
        else:
            df = pd.DataFrame(rows)[list(trade_detail_dict.keys())].rename(columns=trade_detail_dict)
        df['市场'] = df['编号'].apply(lambda x: market_num_dict.get(str(x)))
        del df['编号']
        df['时间'] = df['更新时间戳'].apply(lambda x: str(datetime.fromtimestamp(x)))
        del df['更新时间戳']
        # 将object类型转为数值型
        ignore_cols = ['名称', '代码', '市场', '时间']
        df = trans_num(df, ignore_cols)
        return df
    data = pd.DataFrame()
    for i in range(step):
        newdata = inner(code_ids[i*DIV:(i+1)*DIV])
        data = pd.concat([data, newdata], ignore_index=True)
    return data

# 将接口market_indics和stock_indics封装在一起
# 获取指定市场所有标的或单个或多个证券最新行情指标
def realtime_data(market='沪深A', code=None):
    '''获取指定市场所有标的或单个或多个证券最新行情指标
    market表示行情名称或列表，默认沪深A股
    '沪深京A':沪深京A股市场行情; '沪深A':沪深A股市场行情;'沪A':沪市A股市场行情
    '深A':深市A股市场行情;北A :北证A股市场行情;'可转债':沪深可转债市场行情;
    '期货':期货市场行情;'创业板':创业板市场行情;'美股':美股市场行情;
    '港股':港股市场行情;'中概股':中国概念股市场行情;'新股':沪深新股市场行情;
    '科创板':科创板市场行情;'沪股通' 沪股通市场行情;'深股通':深股通市场行情;
    '行业板块':行业板块市场行情;'概念板块':概念板块市场行情;
    '沪深指数':沪深系列指数市场行情;'上证指数':上证系列指数市场行情
    '深证指数':深证系列指数市场行情;'ETF' ETF基金市场行情;'LOF' LOF 基金市场行情
    code:输入单个或多个证券的list，不输入参数，默认返回某市场实时指标
    如code='中国平安'，或code='000001'，或code=['中国平安','晓程科技','东方财富']
    '''
    if code is None:
        return market_realtime(market)
    else:
        return stock_realtime(code)


# 获取单只证券最新交易日日内数据
def intraday_data(code):
    """
    code可以为股票、期货、债券代码简称或代码，如晓程科技或300139
    也可以是多个股票或期货或债券的list,如['300139','西部建设','云南铜业']
    返回股票、期货、债券的最新交易日成交情况
    """
    max_count = 10000000
    code_id = get_code_id(code)
    columns = ['名称', '代码', '时间', '昨收', '成交价', '成交量', '单数']
    params = (
        ('secid', code_id),
        ('fields1', 'f1,f2,f3,f4,f5'),
        ('fields2', 'f51,f52,f53,f54,f55'),
        ('pos', f'-{int(max_count)}')
    )

    response = session.get(
        'https://push2.eastmoney.com/api/qt/stock/details/get', params=params)

    res = response.json()
    texts = res['data']['details']
    rows = [txt.split(',')[:4] for txt in texts]
    df = pd.DataFrame(columns=columns, index=range(len(rows)))
    df.loc[:, '代码'] = code_id.split('.')[1]
    df.loc[:, '名称'] = stock_info(code)['名称']
    detail_df = pd.DataFrame(rows, columns=['时间', '成交价', '成交量', '单数'])
    detail_df.insert(1, '昨收', res['data']['prePrice'])
    df.loc[:, detail_df.columns] = detail_df.values
    # 将object类型转为数值型
    ignore_cols = ['名称', '代码', '时间']
    df = trans_num(df, ignore_cols)
    return df


# 获取个股当天实时交易快照数据
def stock_snapshot(code):
    """
    获取沪深市场股票最新行情快照
    code:股票代码
    """
    code = get_code_id(code).split('.')[1]
    params = (
        ('id', code),
        ('callback', 'jQuery183026310160411569883_1646052793441'),
    )
    columns = {
        'code': '代码',
        'name': '名称',
        'time': '时间',
        'zd': '涨跌额',
        'zdf': '涨跌幅',
        'currentPrice': '最新价',
        'yesClosePrice': '昨收',
        'openPrice': '今开',
        'open': '开盘',
        'high': '最高',
        'low': '最低',
        'avg': '均价',
        'topprice': '涨停价',
        'bottomprice': '跌停价',
        'turnover': '换手率',
        'volume': '成交量',
        'amount': '成交额',
        'sale1': '卖1价',
        'sale2': '卖2价',
        'sale3': '卖3价',
        'sale4': '卖4价',
        'sale5': '卖5价',
        'buy1': '买1价',
        'buy2': '买2价',
        'buy3': '买3价',
        'buy4': '买4价',
        'buy5': '买5价',
        'sale1_count': '卖1数量',
        'sale2_count': '卖2数量',
        'sale3_count': '卖3数量',
        'sale4_count': '卖4数量',
        'sale5_count': '卖5数量',
        'buy1_count': '买1数量',
        'buy2_count': '买2数量',
        'buy3_count': '买3数量',
        'buy4_count': '买4数量',
        'buy5_count': '买5数量',
    }
    response = requests.get(
        'https://hsmarketwg.eastmoney.com/api/SHSZQuoteSnapshot', params=params)
    start_index = response.text.find('{')
    end_index = response.text.rfind('}')

    s = pd.Series(index=columns.values(), dtype='object')
    try:
        data = json.loads(response.text[start_index:end_index + 1])
    except:
        return s
    if not data.get('fivequote'):
        return s
    d = {**data.pop('fivequote'), **data.pop('realtimequote'), **data}
    ss = pd.Series(d).rename(index=columns)[columns.values()]
    str_type_list = ['代码', '名称', '时间']
    all_type_list = columns.values()
    for column in (set(all_type_list) - set(str_type_list)):
        ss[column] = str(ss[column]).strip('%')
    df = pd.DataFrame(ss).T
    # 将object类型转为数值型
    ignore_cols = ['名称', '代码', '时间']
    df = trans_num(df, ignore_cols)
    return df


# 获取最近n日（最多五天）的1分钟数据
def get_1min_data(code, n=5):
    """
    获取股票、期货、债券的最近n日的1分钟K线行情
    code : 代码、名称
    n: 默认为 1,最大为 5
    """
    intraday_dict = {
        'f51': '日期',
        'f52': '开盘',
        'f53': '收盘',
        'f54': '最高',
        'f55': '最低',
        'f56': '成交量',
        'f57': '成交额', }
    fields = list(intraday_dict.keys())
    columns = list(intraday_dict.values())
    fields2 = ",".join(fields)
    n = n if n <= 5 else 5
    code_id = get_code_id(code)
    params = (
        ('fields1', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13'),
        ('fields2', fields2),
        ('ndays', n),
        ('iscr', '0'),
        ('iscca', '0'),
        ('secid', code_id),
    )

    res = session.get('http://push2his.eastmoney.com/api/qt/stock/trends2/get',
                      params=params).json()

    data = jsonpath(res, '$..trends[:]')
    if not data:
        columns.insert(0, '代码')
        columns.insert(0, '名称')
        return pd.DataFrame(columns=columns)

    rows = [d.split(',') for d in data]
    name = res['data']['name']
    code = code_id.split('.')[-1]
    df = pd.DataFrame(rows, columns=columns)
    df.insert(0, '代码', code)
    df.insert(0, '名称', name)
    cols1 = ['日期', '名称', '代码', '开盘', '最高', '最低', '收盘', '成交量', '成交额']
    cols2 = ['date', 'name', 'code', 'open', 'high', 'low', 'close', 'vol', 'turnover']
    df = df.rename(columns=dict(zip(cols1, cols2)))
    df.index = pd.to_datetime(df['date'])
    df = df[cols2[1:]]
    # 将object类型转为数值型
    ignore_cols = ['name', 'code']
    df = trans_num(df, ignore_cols)
    return df

# 获取股票、债券、期货、基金历史K线数据
def quant_data(code, start='19000101', end=None, freq='d', fqt=1):
    """
    获取股票、指数、债券、期货、基金等历史K线行情
    code: 可以是股票或指数（包括美股港股等）代码或简称
    start、end: 起始和结束日期，年月日
    freq: 时间频率，默认日, 60 : 60 分钟；101或'D'或'd'：日；102或‘w’或'W'：周; 103或'm'或'M': 月
    fqt: 复权类型，0：不复权，1：前复权；2：后复权，默认前复权
    """
    standard = {
        "open": [],
        "close": [],
        "high": [],
        "low": [],
        "volume": []
    }
    try:
        if end in [None,'']:
            end=latest_trade_date()
        start = ''.join(start.split('-'))
        end = ''.join(end.split('-'))

        if type(freq) == str:
            freq = freq.lower()
            if freq == 'd':
                freq = 101
            elif freq == 'w':
                freq = 102
            elif freq == 'm':
                freq = 103
            else:
                print('时间频率输入有误')
        
        code_id = get_code_id(code)

        kline_field = {
            'f51': 'date',
            'f52': 'open',
            'f53': 'close',
            'f54': 'high',
            'f55': 'low',
            'f57': 'volume',
        }

        fields = list(kline_field.keys())
        columns = list(kline_field.values())

        fields2 = ",".join(fields)

        params = (
            ('fields1', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13'),
            ('fields2', fields2),
            ('beg', start),
            ('end', end),
            ('rtntype', '6'),
            ('secid', code_id),
            ('klt', f'{freq}'),
            ('fqt', f'{fqt}'),
        )

        url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get'
        # 多线程装饰器
        json_response = session.get(
            url, headers=request_header, params=params).json()
        date = []
        for line in json_response["data"]["klines"]:
            tmp = line.split(",")
            #print(tmp)
            standard["open"].append(tmp[1])
            standard["close"].append(tmp[2])
            standard["high"].append(tmp[3])
            standard["low"].append(tmp[4])
            standard["volume"].append(tmp[5])
            date.append(tmp[0])
    except Exception as e:
        print (e)
    result = {k: np.asarray(v, dtype='double') for k, v in standard.items()}
    result["date"] = date
    return result


# 获取股票、债券、期货、基金历史K线数据
def web_data(code, start='19000101', end=None, freq='d', fqt=1):
    """
    获取股票、指数、债券、期货、基金等历史K线行情
    code可以是股票或指数（包括美股港股等）代码或简称
    start和end为起始和结束日期，年月日
    freq:时间频率，默认日，1 : 分钟；5 : 5 分钟；15 : 15 分钟；30 : 30 分钟；
    60 : 60 分钟；101或'D'或'd'：日；102或‘w’或'W'：周; 103或'm'或'M': 月
    注意1分钟只能获取最近5个交易日一分钟数据
    fqt:复权类型，0：不复权，1：前复权；2：后复权，默认前复权
    """
    if end in [None,'']:
        end=latest_trade_date()
    if freq == 1:
        return get_1min_data(code)
    start = ''.join(start.split('-'))
    end = ''.join(end.split('-'))
    if type(freq) == str:
        freq = freq.lower()
        if freq == 'd':
            freq = 101
        elif freq == 'w':
            freq = 102
        elif freq == 'm':
            freq = 103
        else:
            print('时间频率输入有误')
    kline_field = {
        'f51': '日期',
        'f52': '开盘',
        'f53': '收盘',
        'f54': '最高',
        'f55': '最低',
        'f56': '成交量',
        'f57': '成交额',
        'f58': '振幅',
        'f59': '涨跌幅',
        'f60': '涨跌额',
        'f61': '换手率'}
    fields = list(kline_field.keys())
    columns = list(kline_field.values())
    cols1 = ['日期', '名称', '代码', '开盘', '最高', '最低', '收盘', '成交量', '成交额', '换手率']
    cols2 = ['date', 'name', 'code', 'open', 'high', 'low', 'close', 'volume', 'turnover', 'turnover_rate']
    fields2 = ",".join(fields)
    code_id = get_code_id(code)
    params = (
        ('fields1', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13'),
        ('fields2', fields2),
        ('beg', start),
        ('end', end),
        ('rtntype', '6'),
        ('secid', code_id),
        ('klt', f'{freq}'),
        ('fqt', f'{fqt}'),
    )

    url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get'
    # 多线程装饰器

    json_response = session.get(
        url, headers=request_header, params=params).json()
    klines = jsonpath(json_response, '$..klines[:]')
    if not klines:
        columns.insert(0, '代码')
        columns.insert(0, '名称')
        return pd.DataFrame(columns=cols2)

    rows = [k.split(',') for k in klines]
    name = json_response['data']['name']
    code = code_id.split('.')[-1]
    df = pd.DataFrame(rows, columns=columns)

    df.insert(0, '代码', code)
    df.insert(0, '名称', name)

    df = df.rename(columns=dict(zip(cols1, cols2)))
    # print(df)
    # df.index = pd.to_datetime(df['date'])
    # df = df[cols2[1:]]
    df = df[cols2]
    # print(df)    
    # 将object类型转为数值型
    ignore_cols = ['name', 'code', 'date']
    df = trans_num(df, ignore_cols)
    return df

# 获取单只或多只证券（股票、基金、债券、期货)的收盘价格dataframe
def get_price(code_list, start='19000101', end=None, freq='d', fqt=1):
    '''code_list输入股票list列表
    如code_list=['中国平安','贵州茅台','工业富联']
    '''
    if isinstance(code_list, str):
        code_list = [code_list]
    
    if end is None:
        end=latest_trade_date()

    @multitasking.task
    def run(code):
        try:
            temp = web_data(code, start, end, freq, fqt)
            temp[temp.name[0]]=temp.close
            data_list.append(temp[temp.name[0]])
        except:
            pass

    data_list = []
    for code in tqdm(code_list):
        try:
            run(code)
        except:
            continue
    multitasking.wait_for_tasks()
    # 转换为dataframe
    df = pd.concat(data_list, axis=1)
    return df

# 获取单只或多只证券（股票、基金、债券、期货)的历史K线数据
def get_data(code_list, start='19000101', end=None, freq='d', fqt=1):
    '''code_list输入股票list列表
    如code_list=['中国平安','贵州茅台','工业富联']
    返回多只股票多期时间的面板数据
    '''
    if isinstance(code_list, str):
        code_list = [code_list]
    if end is None:
        end=latest_trade_date()

    data_list = []

    @multitasking.task
    def run(code):
        data = web_data(code, start, end, freq, fqt)
        data_list.append(data)

    for code in tqdm(code_list):
        run(code)
    multitasking.wait_for_tasks()
    # 转换为dataframe
    df = pd.concat(data_list, axis=0)
    return df

def index_member(code):
    """
    获取指数成分股信息
    code : 指数名称或者指数代码
    """
    fields = {
        'IndexCode': '指数代码',
        'IndexName': '指数名称',
        'StockCode': '股票代码',
        'StockName': '股票名称',
        'MARKETCAPPCT': '股票权重'
    }
    code_id = get_code_id(code).split('.')[1]
    params = (
        ('IndexCode', code_id),
        ('pageIndex', '1'),
        ('pageSize', '10000'),
        ('deviceid', '1234567890'),
        ('version', '6.9.9'),
        ('product', 'EFund'),
        ('plat', 'Iphone'),
        ('ServerVersion', '6.9.9'),
    )
    url = 'https://fundztapi.eastmoney.com/FundSpecialApiNew/FundSpecialZSB30ZSCFG'
    res = requests.get(
        url,
        params=params,
        headers=request_header).json()
    data = res['Datas']
    if not data:
        return
    df = pd.DataFrame(data).rename(
        columns=fields)[fields.values()]
    df['股票权重'] = pd.to_numeric(df['股票权重'], errors='coerce')
    return df

# 龙虎榜详情数据
def stock_billboard(start=None, end=None):
    '''起始和结束日期默认为None，表示最新，日期格式'2021-08-21'
    '''
    # 如果输入日期没有带'-'连接符，转换一下
    date_trans = lambda s: '-'.join([s[:4], s[4:6], s[6:]])
    if start is not None:
        if '-' not in start:
            start = date_trans(start)
    if end is not None:
        if '-' not in end:
            end = date_trans(end)

    today = datetime.today().date()
    mode = 'auto'
    if start is None:
        start_date = today

    if end is None:
        end_date = today

    if isinstance(start, str):
        mode = 'user'
        start_date = datetime.strptime(start, '%Y-%m-%d')
    if isinstance(end, str):
        mode = 'user'
        end_date = datetime.strptime(end, '%Y-%m-%d')

    fields = {
        'SECURITY_CODE': '股票代码',
        'SECURITY_NAME_ABBR': '股票名称',
        'TRADE_DATE': '上榜日期',
        'EXPLAIN': '解读',
        'CLOSE_PRICE': '收盘价',
        'CHANGE_RATE': '涨跌幅',
        'TURNOVERRATE': '换手率',
        'BILLBOARD_NET_AMT': '龙虎榜净买额',
        'BILLBOARD_BUY_AMT': '龙虎榜买入额',
        'BILLBOARD_SELL_AMT': '龙虎榜卖出额',
        'BILLBOARD_DEAL_AMT': '龙虎榜成交额',
        'ACCUM_AMOUNT': '市场总成交额',
        'DEAL_NET_RATIO': '净买额占总成交比',
        'DEAL_AMOUNT_RATIO': '成交额占总成交比',
        'FREE_MARKET_CAP': '流通市值',
        'EXPLANATION': '上榜原因'
    }
    bar = None
    while True:
        dfs = []
        page = 1
        while 1:
            params = (
                ('sortColumns', 'TRADE_DATE,SECURITY_CODE'),
                ('sortTypes', '-1,1'),
                ('pageSize', '500'),
                ('pageNumber', page),
                ('reportName', 'RPT_DAILYBILLBOARD_DETAILS'),
                ('columns', 'ALL'),
                ('source', 'WEB'),
                ('client', 'WEB'),
                ('filter',
                 f"(TRADE_DATE<='{end_date}')(TRADE_DATE>='{start_date}')"),
            )

            url = 'http://datacenter-web.eastmoney.com/api/data/v1/get'

            response = session.get(url, params=params)
            if bar is None:
                pages = jsonpath(response.json(), '$..pages')

                if pages and pages[0] != 1:
                    total = pages[0]
                    bar = tqdm(total=int(total))
            if bar is not None:
                bar.update()

            items = jsonpath(response.json(), '$..data[:]')
            if not items:
                break
            page += 1
            df = pd.DataFrame(items).rename(columns=fields)[fields.values()]
            dfs.append(df)
        if mode == 'user':
            break
        if len(dfs) == 0:
            start_date = start_date - timedelta(1)
            end_date = end_date - timedelta(1)

        if len(dfs) > 0:
            break
    if len(dfs) == 0:
        df = pd.DataFrame(columns=fields.values())
        return df

    df = pd.concat(dfs, ignore_index=True)
    df['上榜日期'] = df['上榜日期'].astype('str').apply(lambda x: x.split(' ')[0])
    # 保留需要的数据特征
    cols = ['股票代码', '股票名称', '上榜日期', '收盘价', '涨跌幅', '换手率',
            '龙虎榜净买额', '流通市值', '上榜原因', '解读']
    # 有些股票可能因不同原因上榜，剔除重复记录样本
    df = df[cols].drop_duplicates(['股票代码', '上榜日期'])
    # 剔除退市、B股和新股N
    s1 = df['股票名称'].str.contains('退')
    s2 = df['股票名称'].str.contains('B')
    s3 = df['股票名称'].str.contains('N')
    s = s1 | s2 | s3
    df = df[-(s)]
    return df


#获取沪深指数对应代码名称字典
def index_code_name():
    df=realtime_data('沪深指数')
    code_name_dict=dict((df[['代码','名称']].values))
    return code_name_dict

#获取指数历史交易数据
def get_index_data(code_list, start='19000101', end=None, freq='d'):
    
    if isinstance(code_list, str):
        code_list = [code_list]
    if end is None:
        end=latest_trade_date()

    data_list = []

    @multitasking.task
    def run(code):
        data = web_data(code, start=start, end=end, freq=freq)
        data_list.append(data)

    for code in tqdm(code_list):
        if code.isdigit():
            code_name_dict=index_code_name()
            code=code_name_dict[code]
        run(code)
    multitasking.wait_for_tasks()
    # 转换为dataframe
    df = pd.concat(data_list, axis=0)
    return df

# 获取指数价格数据
def get_index_price(code_list, start='19000101', end=None, freq='d'):
    '''code_list输入指数list列表
    '''
    
    if isinstance(code_list, str):
        code_list = [code_list]
    
    if end is None:
        end=latest_trade_date()

    @multitasking.task
    def run(code):
        try:
            temp = web_data(code, start, end, freq)
            temp[temp.name[0]]=temp.close
            data_list.append(temp[temp.name[0]])
        except:
            pass

    data_list = []
    for code in tqdm(code_list):
        if code.isdigit():
            code_name_dict=index_code_name()
            code=code_name_dict[code]
        try:
            run(code)
        except:
            continue
    multitasking.wait_for_tasks()
    # 转换为dataframe
    df = pd.concat(data_list, axis=1)
    return df

# 获取单只股票最新交易日的日内分钟级单子流入流出数据
def intraday_money(code):
    """## chinese: 获取股票分钟级流入流出数据|股票分钟级流入流出
    ## english: Get incoming or outcoming of stock today
    ## args: 
        code: 股票名称 
    ## extra:  
        pass
    """
    code_id = get_code_id(code)
    if not code_id:
        return "Not Found Data"    
    params = (
        ('lmt', '0'),
        ('klt', '1'),
        ('secid', code_id),
        ('fields1', 'f1,f2,f3,f7'),
        ('fields2', 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63'),
    )
    url = 'http://push2.eastmoney.com/api/qt/stock/fflow/kline/get'
    res = session.get(url,
                      headers=request_header,
                      params=params).json()
    columns = ['时间', '主力净流入', '小单净流入', '中单净流入', '大单净流入', '超大单净流入']
    name = jsonpath(res, '$..name')[0]
    code = code_id.split('.')[-1]
    data = jsonpath(res, '$..klines[:]')
    if not data:
        columns.insert(0, '代码')
        columns.insert(0, '名称')
        return pd.DataFrame(columns=columns)
    rows = [d.split(',') for d in data]
    #print(rows)
    df = pd.DataFrame(rows, columns=columns)
    df.insert(0, '代码', code)
    df.insert(0, '名称', name)
    cols = ['代码', '名称', '时间']
    df = trans_num(df, cols)
    return df

# 获取单只股票多个交易日单子流入流出数据
def multiday_moneyflow(code):
    """## chinese: 获取股票分钟级流入流出数据|股票分钟级流入流出
    ## english: Get incoming or outcoming of stock today
    ## args: 
        code: 股票名称 
    ## extra:  
        pass
    """
    code_id = get_code_id(code)
    if not code_id:
        return "Not Found Data"
    
    bills = {
        'f51': '日期',
        'f52': '主力净流入',
        'f53': '小单净流入',
        'f54': '中单净流入',
        'f55': '大单净流入',
        'f56': '超大单净流入',
        'f57': '主力净流入占比',
        'f58': '小单流入净占比',
        'f59': '中单流入净占比',
        'f60': '大单流入净占比',
        'f61': '超大单流入净占比',
        'f62': '收盘价',
        'f63': '涨跌幅'

    }
    params = (
        ('lmt', '0'),
        ('klt', '100'),
        ('secid', code_id),
        ('fields1', 'f1,f2,f3,f7'),
        ('fields2', ",".join(list(bills.keys()))),
    )
    url = 'http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get'
    res = session.get(url,
                      headers=request_header,
                      params=params).json()

    name = jsonpath(res, '$..name')[0]
    code = code_id.split('.')[-1]
    data = jsonpath(res, '$..klines[:]')
    columns = list(bills.values())
    if not data:
        columns.insert(0, '代码')
        columns.insert(0, '名称')
        return pd.DataFrame(columns=columns)

    rows = [d.split(',') for d in data]
    
    df = pd.DataFrame(rows, columns=columns)
    df.insert(0, '代码', code)
    df.insert(0, '名称', name)
    cols = ['代码', '名称', '日期']
    df = trans_num(df, cols)
    return df


# 获取股票所属板块
def stock_sector(code):
    """
    获取股票所属板块
    code : 股票代码或者股票名称
    """
    code_id = get_code_id(code)

    params = (
        ('forcect', '1'),
        ('spt', '3'),
        ('fields', 'f1,f12,f152,f3,f14,f128,f136'),
        ('pi', '0'),
        ('pz', '1000'),
        ('po', '1'),
        ('fid', 'f3'),
        ('fid0', 'f4003'),
        ('invt', '2'),
        ('secid', code_id),
    )

    res = session.get(
        'https://push2.eastmoney.com/api/qt/slist/get', params=params)
    df = pd.DataFrame(res.json()['data']['diff']).T
    df.index = range(len(df))
    filelds = {
        'f12': '板块代码',
        'f14': '板块名称',
        'f3': '板块涨幅',
    }
    df = df.rename(columns=filelds)[filelds.values()]
    code = code_id.split('.')[-1]
    # df.insert(0, '股票名称', name)
    df.insert(1, '股票代码', code)
    df['板块涨幅'] = (df['板块涨幅'].astype('float') / 100)
    return df


####可转债历史K线和实时交易数据可通过统一接口get_k_data和intraday_data获取

#########################################################################
####期货future
def future_info():
    '''返回期货'代码', '名称', '涨幅', '最新','ID','市场','时间'
    '''
    df = market_realtime('future')
    cols = ['代码', '名称', '涨幅', '最新', 'ID', '市场', '时间']
    return df[cols]

####期货历史K线和实时交易数据可通过统一接口get_k_data和intraday_data获取

def stock_code_dict():
    df = market_realtime()
    name_code = dict(df[['名称', '代码']].values)
    return name_code