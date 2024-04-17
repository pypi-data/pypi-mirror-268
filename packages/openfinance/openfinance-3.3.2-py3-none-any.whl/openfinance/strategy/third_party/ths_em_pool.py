# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:53:55 2022
author: zhubin_n@outlook.com
"""
import requests
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup
from openfinance.datacenter.database import EMPTY_DATA
from openfinance.datacenter.database.source.eastmoney.util import (
    trans_num,
    latest_trade_date
)
from openfinance.datacenter.database.source.ths.util import ths_header
from openfinance.datacenter.knowledge.decorator import register

@register(name="查询向上突破的股票", description="Get stock starting to rise", graph_node=False)
def get_break_up_stock(duration):
    """## chinese: 查询向上突破的股票
    ## english: Get stock starting to rise
    ## args: 
        duration: 数字天数
    ## extra:
    """
    #print(duration)
    try:
        duration = duration.strip()
        if duration in "5, 10, 20, 30, 60, 90, 250, 500":
            return ths_break_ma('xstp', duration)
        else:
            return ths_break_ma('xstp', 20)
    except:
        return EMPTY_DATA

@register(name="查询向下突破的股票", description="Get stock starting to drop", graph_node=False)
def get_break_down_stock(duration):
    """## chinese: 查询向下突破的股票
    ## english: Get stock starting to drop
    ## args: 
        duration: 数字天数
    ## extra:
    """
    try:
        duration = duration.strip()
        if duration in "5, 10, 20, 30, 60, 90, 250, 500":
            return ths_break_ma('xxtp', duration)
        else:
            return ths_break_ma('xxtp', 20)
    except:
        return EMPTY_DATA

@register(name="查询创新高的股票", description="Get stock with highest price", graph_node=False)
def new_high_stock(data):
    """## chinese: 查询创新高的股票
    ## english: Get stock with highest price
    ## args:
        data: 历史新高, 一年新高, 半年新高, 创月新高
    ## extra:
    """
    try:
        data = data.strip()
        if "历史新高" in data:
            return ths_break_price('cxg', 1)
        elif "一年新高" in data:
            return ths_break_price('cxg', 2)
        elif "半年新高" in data:
            return ths_break_price('cxg', 3)    
        elif "创月新高" in data:
            return ths_break_price('cxg', 4)
        
        return ths_break_price('cxg', 1)
    except:
        return EMPTY_DATA

@register(name="查询历史新低的股票", description="Get stock with new lowest price", graph_node=False)
def new_low_stock(data):
    """## chinese: 查询历史新低的股票
    ## english: Get stock with new lowest price 
    ## args:
        data: 历史新低, 一年新低, 半年新低, 创月新低  
    ## extra:
    """
    try:
        data = data.strip()
        if "历史新低" in data:
            return ths_break_price('cxd', 1)
        elif "一年新低" in data:
            return ths_break_price('cxd', 2)
        elif "半年新低" in data:
            return ths_break_price('cxd', 3)    
        elif "创月新低" in data:
            return ths_break_price('cxd', 4)

        return ths_break_price('cxd', 1)
    except:
        return EMPTY_DATA

#############################################################################
headers=ths_header()
url0='http://data.10jqka.com.cn/rank/'

def fetch_ths_data(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    '''
    try:
        total_page = soup.find(
            "span", attrs={"class": "page_info"}
        ).text.split("/")[1]
    except:
        total_page = 1
    '''
    total_page = 1
    df = pd.DataFrame()
    for page in tqdm(range(1, int(total_page) + 1), leave=False):
        r = requests.get(url, headers=headers)
        temp_df = pd.read_html(r.text)[0]
        df = pd.concat([df, temp_df], ignore_index=True)
    return df

# not to include in recall
def ths_break_ma(flag='xstp', n=20):
    """## chinese: 查询向上突破/或者向下突破的股票
    ## english: Get stock starting to rise
    ## args: 
        flag='xstp':向上突破；'xxtp':向下突破
    ## extra:
        n:可选5、10、20、30、60、90、250、500,表示突破n日均线    
    """
    try:
        page=1
        url =url0+ f"{flag}/board/{n}/order/asc/ajax/1/free/1/page/{page}/free/1/"
        df=fetch_ths_data(url)
        df.columns = ["序号","股票代码","股票简称","最新价","成交额","成交量(万)",
            "涨跌幅","换手率",]
        df["股票代码"] = df["股票代码"].astype(str).str.zfill(6)
        df[["涨跌幅","换手率"]] = df[["涨跌幅","换手率"]].apply(lambda s:s.astype(str).str.strip("%"))
        df['成交量(万)']=df['成交量(万)'].astype(str).str.strip("万")
        del df['成交额']
        ignore_cols = ["股票代码","股票简称"]
        df = trans_num(df, ignore_cols)
        return df.iloc[:,1:].to_string()
    except:
        return EMPTY_DATA

################# No suit for llm right now, need to retreat ###############

#同花顺技术选股持续放量（缩量）
def ths_vol_change(flag='cxfl'):
    """## chinese: 获取持续放量或者缩量的股票
    ## english: Get stock with rising volume
    ## args: 
        flag: 持续放量, 持续缩量
    ## extra:
    """
    flag = flag.strip()
    if "持续缩量" in flag:
        flag = 'cxsl'
    else:
        flag = 'cxfl'

    page=1
    url =url0+ f"{flag}/field/count/order/desc/ajax/1/free/1/page/{page}/free/1/"
    df=fetch_ths_data(url)
        
    df.columns = ["序号","股票代码","股票简称","涨跌幅","最新价","成交量",
        "基准日成交量","天数","阶段涨跌幅","所属行业",]
    df["股票代码"] = df["股票代码"].astype(str).str.zfill(6)
    df["涨跌幅"] = df["涨跌幅"].astype(str).str.strip("%")
    df["阶段涨跌幅"] = df["阶段涨跌幅"].astype(str).str.strip("%")
    ignore_cols = ["股票代码","股票简称","所属行业"]
    df = trans_num(df, ignore_cols)
    return df.iloc[:,1:]


def ths_price_vol(flag='ljqs'):
    """## chinese: 查询量价齐升（齐跌）的股票
    ## english: Get stock with rising price and volume
    ## args: 
        flag: 量价齐升, 量价齐跌
    ## extra:
    """
    flag = flag.strip()

    if "量价齐跌" in flag:
        flag = 'ljqd'
    else:
        flag = 'ljqs'
    page=1
    url = url0+f"{flag}/field/count/order/desc/ajax/1/free/1/page/{page}/free/1/"
    df=fetch_ths_data(url)
        
    df.columns = ["序号","股票代码","股票简称","最新价",
        "天数","阶段涨幅","累计换手率","所属行业",]
    df["股票代码"] = df["股票代码"].astype(str).str.zfill(6)
    df["阶段涨幅"] = df["阶段涨幅"].astype(str).str.strip("%")
    df["累计换手率"] = df["累计换手率"].astype(str).str.strip("%")
    ignore_cols = ["股票代码","股票简称","所属行业",]
    df = trans_num(df, ignore_cols)
    return df.iloc[:,1:]

def ths_stock_money(n=None):
    """
    获取同花顺个股资金流向
    http://data.10jqka.com.cn/funds/ggzjl/#refCountId=data_55f13c2c_254
    n: None、3、5、10、20分别代表 “即时”, "3日排行", "5日排行", "10日排行", "20日排行"
    """
    url = "http://data.10jqka.com.cn/funds/ggzjl/field/zdf/order/desc/ajax/1/free/1/"
    res = requests.get(url, headers=ths_header())
    soup = BeautifulSoup(res.text, "lxml")
    raw_page = soup.find("span", attrs={"class": "page_info"}).text
    page_num = raw_page.split("/")[1]
        
    df = pd.DataFrame()
    for page in tqdm(range(1, int(page_num) + 1)):
        if n is None:
            url = f"http://data.10jqka.com.cn/funds/ggzjl/field/zdf/order/desc/page/{page}/ajax/1/free/1/"
        else:
            url = f"http://data.10jqka.com.cn/funds/ggzjl/board/{n}/field/zdf/order/desc/page/{page}/ajax/1/free/1/"
        r = requests.get(url, headers=ths_header())
        temp_df = pd.read_html(r.text)[0]
        df = pd.concat([df, temp_df], ignore_index=True)

    del df["序号"]
    df.reset_index(inplace=True)
    df["index"] = range(1, len(df) + 1)
    if n is None:
        df.columns = ["序号","代码","简称","最新价", "涨幅","换手率",
            '流入资金','流出资金','净额(万)','成交额',]
    else:
        df.columns = ["序号","代码","简称","最新价","涨幅",
            "换手率","净额(万)",]
    cols=["代码","简称","最新价", "涨幅","换手率",'净额(万)']    
    df=df[cols]
    df["代码"] = df["代码"].astype(str).str.zfill(6)
    df['净额(万)']=df['净额(万)'].apply(lambda s:float(
                s.strip('亿'))*10000 if s.endswith('亿') 
                    else s.strip('万'))
    df[['涨幅','换手率']]=df[['涨幅','换手率']].apply(lambda s:s.str.strip('%'))
    
    ignore_cols = ["代码","简称"]
    df = trans_num(df, ignore_cols)
    return df


def ths_xzjp():
    """## chinese: 查询险资举牌的股票
    ## english: Get stock with insurance company holds
    ## args:
    ## extra:
    """
    url = "http://data.10jqka.com.cn/ajax/xzjp/field/DECLAREDATE/order/desc/ajax/1/free/1/"
    df=fetch_ths_data(url)
        
    df.columns = ["序号","举牌公告日","股票代码","股票简称","现价","涨跌幅",
        "举牌方","增持数量(万)","交易均价","增持数量占总股本比例","变动后持股总数(万)",
        "变动后持股比例","历史数据",]
    df["股票代码"] = df["股票代码"].astype(str).str.zfill(6)
    df["涨跌幅"] = df["涨跌幅"].astype(str).str.zfill(6)
    df["增持数量占总股本比例"] = df["增持数量占总股本比例"].astype(str).str.strip("%")
    df["增持数量(万)"] = df["增持数量(万)"].astype(str).str.strip("万").astype(float)
    df["变动后持股总数(万)"] = df["变动后持股总数(万)"].apply(lambda s: float(s.strip("亿"))*10000 
                                if s.endswith('亿') else float(s.strip("万")) )
    df["变动后持股比例"] = df["变动后持股比例"].astype(str).str.strip("%")
    
    df["举牌公告日"] = pd.to_datetime(df["举牌公告日"]).dt.date
    del df["历史数据"]
    ignore_cols = ["股票代码","股票简称","举牌方","举牌公告日"]
    df = trans_num(df, ignore_cols)
    return df.iloc[:,1:]


#同花顺股票池
def ths_pool(ta=None):
    """ ["创月新高", "半年新高", "一年新高", "历史新高","创月新低", "半年新低", "一年新低", "历史新低",'险资举牌''连续上涨','连续下跌','持续放量','持续缩量','量价齐升','量价齐跌','强势股', "突破均线"] 
     突破均线: f'u{n}',f'd{n}',n=
     10、20、30、60、90、250、500,突破n日均线
     如'u20'代表向上突破20日均线,'d10'：跌破10日均线
     """

    u={"历史新高":1,"一年新高":2,"半年新高":3,"创月新高":4}
    d={"历史新低":1,"一年新低":2,"半年新低":3,"创月新低":4}
    ns=[10,20,30,60,90,250,500]
    uns=['u'+str(n) for n in ns]
    dns=['d'+str(n) for n in ns]
    uns_dict=dict(zip(uns,ns))
    dns_dict=dict(zip(dns,ns))
    
    if ta in ['ljqs','量价齐升','ljqd','量价齐跌']:
        try:return ths_price_vol('ljqs')
        except:return ths_price_vol('ljqd')
    elif ta in ['xzjp' ,'险资举牌']:
        return ths_xzjp()
    elif ta in ['lxsz','连续上涨','lxxd','连续下跌']:
        try:return ths_up_down(flag='lxsz')
        except:return ths_up_down(flag='lxxd')
    elif ta in ['cxfl','持续放量','cxsl' ,'持续缩量']:
        try:return ths_vol_change(flag='cxfl')
        except:return ths_vol_change(flag='cxsl')
   
    elif ta in u.keys():
        return ths_break_price(flag= "cxg",n=u[ta])
    elif ta in d.keys():
        return ths_break_price(flag= "cxd",n=d[ta])
    
    elif ta in uns:
        return ths_break_ma(flag='xstp',n=uns_dict[ta])
    elif ta in dns:
        return ths_break_ma(flag='xxtp',n=dns_dict[ta])
    else:
        return get_strong_momentum_stock()


#获取东方财富网涨停（跌停）板股票池
def limit_pool(flag='u',date=None):
    '''date：日期如'20220916'
    flag='u'代表涨停板,'d'代表跌停,'s'代表强势股
    默认为最新交易日'''
    if date is None:
        date=latest_trade_date()
    if flag=='u' or flag=='up' or flag=='涨停':
        return get_uptick_limit_stock(date)
    elif flag=='d' or flag=='down' or flag=='跌停':
        return get_downtick_limit_stock(date)
    else:
        return get_strong_momentum_stock(date)

# inner call
def ths_break_price(flag="cxg", n=2):
    """## chinese: 查询创一年新高的股票
    ## english: Get stock with one year highest price 
    ## args: 
        flag: 'cxg'：创新高,'cxd'：创新低
    ## extra:
        n=1,2,3,4,分别对应：历史新高（低）、一年新高（低）、半年新高（低）、创月新高（低）    
    """
    page=1
    url = url0+f"{flag}/board/{n}/field/stockcode/order/asc/page/{page}/ajax/1/free/1/"
    df=fetch_ths_data(url)
        
    df.columns = ["序号","股票代码","股票简称","涨跌幅","换手率","最新价",
        "前期点位","前期点位日期",]
    
    df["股票代码"] = df["股票代码"].astype(str).str.zfill(6)
    df["涨跌幅"] = df["涨跌幅"].str.strip("%")
    df["换手率"] = df["换手率"].str.strip("%")
    df["前期点位日期"] = pd.to_datetime(df["前期点位日期"]).dt.date
    # 将object类型转为数值型
    ignore_cols = ["股票代码","股票简称","前期点位日期"]
    df = trans_num(df, ignore_cols)
    return df.iloc[:,1:]

def ths_up_down(flag='lxsz'):
    """## chinese: 查询连续上涨/下跌的股票
    ## english: Get continuous rising stock 
    ## args: 
        flag: 连续上涨, 连续下跌
    ## extra:
    """
    flag = flag.strip()
    if "连续下跌" in flag:
        flag = 'lxxd'
    else:
        flag = 'lxsz'
    page=1
    url = url0+f"{flag}/field/lxts/order/desc/page/{page}/ajax/1/free/1/"
    df=fetch_ths_data(url)
    
    df.columns = ["序号", "股票代码","股票简称","收盘价","最高价",
        "最低价","连涨天数","连续涨跌幅","累计换手率","所属行业",]
    df["股票代码"] = df["股票代码"].astype(str).str.zfill(6)
    df["连续涨跌幅"] = df["连续涨跌幅"].str.strip("%")
    df["累计换手率"] = df["累计换手率"].str.strip("%")
    # 将object类型转为数值型
    ignore_cols = ["股票代码","股票简称","所属行业"]
    df = trans_num(df, ignore_cols)
    return df.iloc[:,1:]