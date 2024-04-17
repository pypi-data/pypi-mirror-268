import requests
import json
import datetime
from bs4 import BeautifulSoup

def get_caijing_news():
    """
        r: Date Source: https://roll.caijing.com.cn
    """    
    url = "https://roll.caijing.com.cn/ajax_lists.php?modelid=0&time=0.3756196327491297"
    headers = {
        "authority": "roll.caijing.com.cn",
        "method": "GET",
        "path": "/ajax_lists.php?modelid=0&time=0.3756196327491297",
        "scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",
        #"accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cookie": "Hm_lvt_b0bfb2d8ed2ed295c7354d304ad369f1=1702369780; __utma=114738197.1386683904.1702369799.1702369799.1702369799.1; __utmc=114738197; __utmz=114738197.1702369799.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=114738197.1.10.1702369799; Hm_lpvt_b0bfb2d8ed2ed295c7354d304ad369f1=1702369799",
        "referer": "https://roll.caijing.com.cn/",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.content
        return content 

def caixing_parse(url):
    headers = {
        "Referer": "http://finance.caijing.com.cn/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode("utf8")
        soup = BeautifulSoup(content, 'html.parser')
        div_tags = soup.find_all('div')
        result = ""
        print(url)
        for div in div_tags:
            divs = div.attrs.get("class", [])
            if len(divs) and divs[0] == "article-content":
                p_tags = div.find_all("p")
                # print("p_tags",p_tags)
                l = len(p_tags)
                for i in range(l):
                    if "免责声明" in p_tags[i].text:
                        continue                    
                    if "img" not in p_tags[i].text:
                        result += p_tags[i].text +"\n"
        return result
        
