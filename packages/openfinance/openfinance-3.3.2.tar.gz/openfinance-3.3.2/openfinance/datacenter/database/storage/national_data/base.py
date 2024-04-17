import json
import requests
import pandas

def government_debt(country="China"):
    """national bond
    """
    url = r'https://data.stats.gov.cn/tablequery.htm?m=QueryData&code=AD07&wds=[{"wdcode":"reg","valuecode":"000000"}]'
    data = requests.get(url, verify=False)
    data = json.loads(data.content)['exceltable']
    result = {
        "DATE": [],
        "FiscalIncome": [],
        "FiscalCost": [],
        "NationalDebt": []
    }
    for item in data:
        if item['col'] == 4:
            if item['row'] == 0:
                result['DATE'].append(item['data'][:-1])
            if item['row'] == 1:                
                result['FiscalIncome'].append(item['data'])
            if item['row'] == 13:                
                result['FiscalCost'].append(item['data'])
            if item['row'] == 28:                
                result['NationalDebt'].append(item['data'])                                                
        if item['col'] == 5:
            if item['row'] == 0:
                result['DATE'].append(item['data'][:-1])
            if item['row'] == 1:                
                result['FiscalIncome'].append(item['data'])
            if item['row'] == 13:                
                result['FiscalCost'].append(item['data'])
            if item['row'] == 28:                
                result['NationalDebt'].append(item['data'])
    return pandas.DataFrame.from_dict(result)



def local_government_debt(country="China"):
    """
    # 债券发行发布平台 https://www.chinabond.com.cn/
    # https://www.celma.org.cn/ydsj/index.jhtml
    debt by province: https://www.governbond.org.cn:4443/api/loadBondData.action?dataType=FDQYDZB&zb=0701&monthSpan=36
    localtotal: https://www.governbond.org.cn:4443/api/loadBondData.action?dataType=YDZB&adCode=87&monthSpan=12&zb=0601
    """
    url = "https://www.governbond.org.cn:4443/api/loadBondData.action?dataType=YDZB&adCode=87&monthSpan=12&zb=0601"
    data = requests.get(url, verify=False)
    data = json.loads(data.content)['data']
    result = {
        "TIME": [],
        "LOCAL_GOV_BOND": [],
    }
    for d in data:
        if d['ZB_ID'] == "0601":
            result["TIME"].append(d['SET_MONTH'])
            result["LOCAL_GOV_BOND"].append(d['AMOUNT'])
    return pandas.DataFrame.from_dict(result)
