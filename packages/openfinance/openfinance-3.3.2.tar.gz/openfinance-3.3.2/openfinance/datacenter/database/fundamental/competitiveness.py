import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper

from openfinance.datacenter.database.fundamental.financial import (
    get_gross_profit_margin,
    get_forecast_predict
)

from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

db = DataBaseManager(Config()).get("db")
ENTITY = EntityGraph()

@register(name="Brand Strength", description="Get Brand Strength of company", zh="品牌价值")
@register(name="Market Share", description="Get Market Share of company", zh="市场份额")
def get_brand_strength(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type:
        date = db.select_by_order(
            table = "t_income_profit_statement where SECURITY_NAME='" + name +"'",
            order_column = "DATE",
            limit_num = 2,
            field = "DATE"
        )[0]['DATE']
        #print(date)
        INDUSTRY_NAME = db.select_one(
            table = "t_income_profit_statement",
            factor_str = "SECURITY_NAME='" +  name + "'",
            field = "INDUSTRY_NAME"
        )['INDUSTRY_NAME']
        #print(INDUSTRY_NAME)
        datas = db.select_by_order(
            table = "t_income_profit_statement where INDUSTRY_NAME='" + INDUSTRY_NAME + "' and DATE='" + date + "'",
            order_column = "TOTAL_OPERATE_INCOME",
            limit_num = 5,
            field = "TOTAL_OPERATE_INCOME,SECURITY_NAME"
        )
        total_len = len(datas)
        brand_rank = f"Brand Strength is not top{total_len} in {INDUSTRY_NAME} market"
        for idx, data in enumerate(datas):
            if name == data["SECURITY_NAME"]:
                brand_rank = f"Brand Strength is top {total_len - idx} in {INDUSTRY_NAME} market"
        return brand_rank
    return
    #print(datas)

@register(name="Competitive Analysis", description="Get Competitive Analysis of company", zh="竞争分析")
def get_competitive_analysis(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        name = ENTITY.get_industry(name)
    if ENTITY.is_industry(name): 
        return 
    return "Competitive Analysis"
