import time
import requests
import json
import pandas as pd

def market_loan_money(code=""):
    url = "http://query.sse.com.cn/commonSoaQuery.do"
    params = {
        "jsonCallBack": "jsonpCallback80463793",
        "isPagination": "true",
        "tabType": "",
        "pageHelp.pageSize": "100",
        "beginDate": "",
        "endDate": "",
        "sqlId": "RZRQ_HZ_INFO",
        "_": "1699521950794"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Cookie": "ba17301551dcbaf9_gdp_user_key=; ba17301551dcbaf9_gdp_session_id=9d1865fc-9f7d-46e8-8909-1e5af0de7334; gdp_user_id=gioenc-badg420c%2C88a5%2C5199%2Cccge%2C4d2c8c3b38e9; ba17301551dcbaf9_gdp_session_id_9d1865fc-9f7d-46e8-8909-1e5af0de7334=true; JSESSIONID=E2061DC64EEC838D10AD23C837BFCF17; ba17301551dcbaf9_gdp_sequence_ids={%22globalKey%22:10%2C%22VISIT%22:2%2C%22PAGE%22:4%2C%22VIEW_CLICK%22:6}",
        "Host": "query.sse.com.cn",
        "Referer": "http://www.sse.com.cn/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.content.decode('utf8')[22:-1]
    data = json.loads(data)['pageHelp']['data']
    df = pd.DataFrame(data)
    cols = {
        "rzye": "Financing_Balance",
        "rqylje": "Financing_Purchase_Amount",
        "rqyl": "Margin_Trading_Balance",
        "rzmre": "Margin_Trading_Balance_Amount",
        "rzche": "Margin_Trading_Sell_Quantity",
        "rzrqjyzl": "Total_Financing_and_Margin_Trading_Balance",
        "opDate": "DATE",
        "rqmcl": "rqmcl"
    }
    df=df[list(cols.keys())].rename(columns=cols)
    return df