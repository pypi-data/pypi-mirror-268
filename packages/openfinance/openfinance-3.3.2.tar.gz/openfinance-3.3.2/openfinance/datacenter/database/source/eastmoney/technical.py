import json
import requests
from bs4 import BeautifulSoup
from openfinance.datacenter.database import EMPTY_DATA
from openfinance.datacenter.database.source.eastmoney.trade import stock_code_dict
from openfinance.datacenter.database.source.eastmoney.util import get_code_id
from openfinance.datacenter.knowledge.decorator import register

# block test ths
def stock_technical_analysis_ths(code):
    """## chinese: 获取股票量价技术分析|量价技术分析
    ## english: Get stock technical analysis|technical analysis
    ## args:
        code: 股票名称
    ## extra: 
    """
    try: 
        code = code.strip()
        if not code.isdigit():
            code=stock_code_dict()[code]    
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.12.2.0 Safari/537.36",
            "Cookie": "PHPSESSID=8e99b69eac20e64f4661ec2f1c9ebafa; cid=8e99b69eac20e64f4661ec2f1c9ebafa1684118067; ComputerID=8e99b69eac20e64f4661ec2f1c9ebafa1684118067; WafStatus=0; guideState=1; ta_random_userid=8f1gt88gnq; other_uid=Ths_iwencai_Xuangu_7nrmjvghfqdu1xdscuaqn4kofi5ptxow; wencai_pc_version=0; THSSESSID=4cfeac70e2d895e5262d0ba155; v=A2huh_iCmJnylbQdfPAoZkOKP11_kc3krvWgHyKZtOPWfQbDyqGcK_4FcKdx"
        }

        url = f"https://www.iwencai.com/diag/block-detail?pid=10331&codes={code}&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A137%7D%7D%7D"
        #print(url)
        data = requests.get(url, headers=headers)
        data = json.loads(data.text)
        #print(data)    
        if data['success']:
            result = data['data']['data']['result']
            comment = result['comment']
            return comment
    except:
        return EMPTY_DATA

#@register(name="Technical Analysis", description="Get stock technical analysis", zh="量价技术分析")
def stock_technical_analysis(code):
    """## chinese: 获取股票量价技术分析|量价技术分析
    ## english: Get stock technical analysis|technical analysis
    ## args: 
        code: 股票名称 
    ## extra:  
        技术形态指标: https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery112302032763064950549_1687337470570&filter=(SECURITY_CODE%3D%22300418%22)&columns=ALL&source=WEB&client=WEB&reportName=PRT_STOCK_MACD_PK&sortColumns=TRADEDATE&sortTypes=-1&pageSize=1&_=1687337470588
    """
    try:    
        code_id = get_code_id(code)[2:]

        url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
        params = {
            "sortColumns": "TRADEDATE",
            "sortTypes": "-1",
            "pageSize": "1",
            "pageNumber": "1",
            "reportName": "PRT_STOCK_MACD_PK",
            "columns": "MACDCOUT,KDJOUT,BOLLOUT,RSIOUT,WROUT",
            "source": "WEB",
            "client": "WEB",
            "filter": f'(SECURITY_CODE="{code_id}")',
            '_': '1687338713167',
        }
        res = requests.get(url, params=params)
        data_json = res.json()
        #print(data_json)
        date = data_json['result']['data'][0]
        print(date)
        result = ""
        if "无明显" not in date['MACDCOUT']:
            result += date['MACDCOUT'] + ", "
        if "无明显" not in date['KDJOUT']:
            result += date['KDJOUT'] + ", "            
        if "无明显" not in date['BOLLOUT']:
            result += date['BOLLOUT'] + ", "
        if "无明显" not in date['RSIOUT']:
            result += date['RSIOUT'] + ", "
        if "无明显" not in date['WROUT']:
            result += date['WROUT'] + ", "
        return result[:-1]
    except:
        return EMPTY_DATA

def get_price_volume_status(code):
    """## chinese: 获取股票量价形态分析|量价形态分析
    ## english: Get price/volume trend|Price Volume Trend
    ## args: 
        code: 股票名称 
    ## extra:  
        价格量级指标 : https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123002449513155562366_1687338292300&filter=(SECURITY_CODE%3D%22300418%22)&columns=ALL&source=WEB&client=WEB&reportName=RPT_STOCK_TRENDVOLUME_PK&sortColumns=TRADE_DATE&sortTypes=-1&pageSize=1&_=1687338292301
        价格趋势量级评论： https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123002449513155562366_1687338292298&filter=(SECUCODE%3D%22300418.SZ%22)&columns=SECUCODE%2CSECURITY_CODE%2CSECURITY_NAME_ABBR%2CTRADE_DATE%2CCOMMENT_TXT&source=WEB&client=WEB&reportName=RPT_STOCK_TRENDVOLUME_COMMENT&pageSize=1&_=1687338292299
    """
    try:
        code_id = get_code_id(code, 2)
        url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
        params = {
            "sortColumns": "TRADE_DATE",
            "sortTypes": "-1",
            "pageSize": "1",
            "pageNumber": "1",
            "reportName": "RPT_STOCK_TRENDVOLUME_COMMENT",
            "columns": "COMMENT_TXT",
            "source": "WEB",
            "client": "WEB",
            "filter": f'(SECUCODE="{code_id}")',
            '_': '1687338713167',
        }
        res = requests.get(url, params=params)
        data_json = res.json()
        return "Price/Volume Trend: " + data_json['result']['data'][0]['COMMENT_TXT']
    except:
        return EMPTY_DATA