import pandas as pd
import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.database.fundamental.news import get_institution_rating
from openfinance.datacenter.database.fundamental.money_flow import get_money_flow

from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum
from openfinance.datacenter.database.source.eastmoney.industry import (
    industry_money_flow, 
    industry_index_trend
)

ENTITY = EntityGraph()
db = DataBaseManager(Config()).get("db")

@register(name="Industry Analysis", description="Get Industry Trend Analysis", zh="行业趋势")
def get_industry_analysis(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    # print(name, entity_type)
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        name = ENTITY.get_industry(name)
    if ENTITY.is_industry(name): 
        return wrapper([
            industry_index_trend(name) 
        ])
    return "Industry Analysis"


def get_gov_stat(name="房地产", entity_type=EntityEnum.Industry.type, **kwargs: Any):
    # "select * from t_news_percept where entity_type='Industry' and entity like '%%房%%' limit 100"
    sql = f"select * from t_gov_stat_hgyd where Datename like '%%{name}%%' limit 20"
    data = db.exec(sql)
    res_str = ""
    for item in data:
        name = item.get('Datename', '')
        res_str += name + ": "
        tmp_dict = dict()
        for key, value in item.items():
            if 'name' not in key:
                tmp_dict[key] = value
        tmp_dict_sort = sorted(tmp_dict.items(), key=lambda x: x[0])
        for info in tmp_dict_sort:
            res_str += 'time: ' + info[0][4:] + ' value: ' + str(info[1]) + ' '
        res_str += '\n'

    return res_str