import requests
import json
import time
import datetime
from bs4 import BeautifulSoup

def get_cailianshe_news():
    """
        r: Date Source: https://www.cls.cn/telegraph
    """
    url = "https://sslecal2.investing.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&category=_employment,_economicActivity,_inflation,_credit,_centralBanks,_confidenceIndex,_balance,_Bonds&importance=2,3&features=datepicker,timezone&countries=37,5&calType=day&timeZone=28&lang=6"

    headers = {
        "Accept": "application/json, text/plain, */*",
        #"Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": "HWWAFSESID=399171ae36ca4a49027; HWWAFSESTIME=1703486246788; vipNotificationState=on; isMinimize=off; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1703486252; hasTelegraphNotification=off; hasTelegraphSound=off; hasTelegraphRemind=off; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1703486328",
        "Origin": "https://sslecal2.investing.com",
        "Referer": "https://sslecal2.investing.com/",
        "Sec-Ch-Ua": 'Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = json.loads(response.content)
        return content


if __name__ == '__main__':
    import time
    infile = open("file.txt", "w")
    docs = list()
    while True:
        jsondata = get_cailianshe_news()
        for d in jsondata["data"]["roll_data"]:
            if d["id"] in docs:
                continue
            if len(docs) == 10:
                docs.pop(0)
            docs.append(d["id"])
            infile.write(d["content"] + "\n")
            infile.write(d["level"] + "\n")
            infile.write(d["title"] + "\n")
            if d["subjects"]:
                for sd in d["subjects"]:
                    infile.write(sd["subject_name"])
            infile.write("\n")
            infile.flush()
        time.sleep(30)