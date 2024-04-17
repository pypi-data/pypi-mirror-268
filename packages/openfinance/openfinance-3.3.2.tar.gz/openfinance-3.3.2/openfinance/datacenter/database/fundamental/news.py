# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:53:48 2022

"""
import time
from typing import Any

from openfinance.config import Config
from openfinance.datacenter.database import EMPTY_DATA
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register

from openfinance.datacenter.database.source.eastmoney.industry import (
    get_industry_by_company
)
from openfinance.datacenter.database.source.eastmoney.news import (
    industry_institutional_rating,
    stock_institutional_rating,
    get_company_news
)
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

ENTITY = EntityGraph()
db = DataBaseManager(Config()).get("db")

def get_recent_news(name="", entity_type=""):
    table = f"t_news_percept where entity_type='{entity_type}'"
    if name:
         table += f" and entity like '%{name}%'"
    fields = "indicator, effect, src, TIME"
    order_column = "TIME"
    data = db.select_by_order(
        table=table,
        order_column = order_column,
        field = fields,
        limit_num = 5
    )
    delta = 3600
    
    result = ""
    for d in data:
        unix_ts = int(d["TIME"].timestamp())
        deltahours = (int(time.time()) - unix_ts) // delta
        result += f"""a {d["effect"]} news about {d["src"]} before {deltahours} hours\n"""
    return result

# need to improve later
@register(name="Institution Rating", description="Get institutional rating", zh="机构评级")
def get_institution_rating(name, entity_type=EntityEnum.Company.type, **kwargs: Any):
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        industryCode = get_industry_by_company(name)
        return industry_institutional_rating(industryCode)
    return stock_institutional_rating(name)

@register(name="Government policies", description="Get Government policies changements", zh="政府监管政策")
@register(name="Recent News", description="Get recent news", zh="公司新闻")
def get_lastest_news(name, entity_type=EntityEnum.Company.type, **kwargs: Any):
    # print(name, entity_type)
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        industry = ENTITY.get_industry(name)
        return get_recent_news(name=industry, entity_type=entity_type)
    elif ENTITY.is_industry(name):
        return get_recent_news(name=name, entity_type=EntityEnum.Industry.type)
    elif ENTITY.is_company_type(entity_type):
        return get_company_news(name)        
    elif ENTITY.is_economy_type(entity_type):
        return get_recent_news(entity_type=entity_type)
    elif ENTITY.is_market_type(entity_type):
        return get_recent_news(entity_type=entity_type)
    return "No Recent News"