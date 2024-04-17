import requests
import pandas as pd
import numpy as np


class FutureSource:
    url = 'http://85.push2.eastmoney.com/api/qt/clist/get'
    params = {
        "pn": 1,
        "pz": 20,
        "po": 1,
        "np": 1,
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": 2,
        "invt": 2,
        "wbp2u": "|0|0|0|web",
        "fid": "f3",
        "fs": "m:10+c:510050",
        "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f28,f11,f62,f128,f136,f115,f152,f133,f108,f163,f161,f162",
        "_": 1709194739122
    }
    fs = {
        "sz300": "m:12 c:159919",
        "sh50": "m:10+c:510050",
        "second_board": "m:12 c:159915",
        "zz500": "m:12 c:159922"
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'qgqp_b_id=164c76d2ed75802b814949a81b3b6191; emshistory=%5B%22%E8%B4%B5%E5%B7%9E%E8%8C%85%E5%8F%B0%22%2C%22%E5%86%B0%E5%B7%9D%E7%BD%91%E7%BB%9C%22%2C%22%E9%AB%98%E6%B5%8B%E8%82%A1%E4%BB%BD%22%2C%22%E7%A7%A6%E5%AE%89%E8%82%A1%E4%BB%BD%22%2C%22%E7%9F%B3%E8%8B%B1%E8%82%A1%E4%BB%BD%22%2C%22%E6%8B%93%E6%96%B0%E8%8D%AF%E4%B8%9A%22%2C%22%E7%94%A8%E6%88%B7%E6%B4%BB%E8%B7%83%E5%BA%A6%E6%B8%B8%E6%88%8F%22%5D; websitepoptg_api_time=1709114347707; st_si=35755659832731; st_asi=delete; HAList=ty-10-10006928-50ETF%u6CBD4%u67082400%2Cty-10-10006919-50ETF%u8D2D4%u67082400%2Cty-10-10006404-50ETF%u8D2D3%u67082400%2Cty-220-IH2409-%u4E0A%u8BC12409%2Cty-104-CN00Y-A50%u671F%u6307%u5F53%u6708%u8FDE%u7EED%2Cty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-1-688309-%u6052%u8A89%u73AF%u4FDD%2Cty-1-603688-%u77F3%u82F1%u80A1%u4EFD%2Cty-0-000333-%u7F8E%u7684%u96C6%u56E2%2Cty-1-600621-%u534E%u946B%u80A1%u4EFD; st_pvi=54709136970065; st_sp=2023-12-19%2015%3A13%3A28; st_inirUrl=http%3A%2F%2Fquote.eastmoney.com%2Fcenter%2Fgridlist.html; st_sn=25; st_psi=20240229163918735-113200301356-5054004340',
        'Host': '85.push2.eastmoney.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }

    def get_future_data(
        self,
        source
    ):
        cols = {
            "f161": "strike",
            "f162": "days",
            "f28": "close",
            #"f16": "close",  # open
            #"f2": "close",  # new
            "f14": "type"
        }
        if source in self.fs:
            self.params.update(
                {
                    "fs": self.fs[source],
                    "pn": 1    
                }
            )
        else:
            return None

        def extract_future(data):
            result = {}
            for k, v in cols.items():
                result[k] = []
            
            for d in data:
                for k, v in cols.items():
                    if k == "f14":
                        if "购" in d[k]:
                            result[k].append("C")
                        elif "沽" in d[k]:
                            result[k].append("P")              
                    else:
                        result[k].append(d[k])
            return pd.DataFrame(result)
        response = requests.get(
            self.url, 
            headers=self.headers, 
            params=self.params
        ).json()
        total = response["data"]["total"]
        df = extract_future(response["data"]["diff"])
        
        pg = int((total + 19)/20)
        for i in range(1, pg):
            self.params.update({"pn": i + 1})
            response = requests.get(
                self.url, 
                headers=self.headers, 
                params=self.params
            ).json()
            df = pd.concat([df, extract_future(response["data"]["diff"])], ignore_index=True)
        df = df.rename(columns=cols)
        # print(df)
        return df
