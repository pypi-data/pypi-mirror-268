import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.echarts import ChartManager
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

from openfinance.datacenter.database.source.eastmoney.fundamental import get_company_valuation
from openfinance.datacenter.database.fundamental.financial import (
    get_forward_pe,
    get_divide
)

db = DataBaseManager(Config()).get("db")

ENTITY = EntityGraph()

def industry_valuation(name):
    datas = db.select_more(
        table = "t_industy_all_valuation",
        range_str = "INDUSTRY_NAME='" + name + "'"
    )
    if len(datas):
        result = ""
        columns = {
            "PE_TTM": "Price to Earning",
            "PS_TTM": "Price to Sales",
            "PCF_OCF_TTM": "Price to cash flow",
            "PEG": "PEG"
        }
        for k, v in columns.items():
            result += v + ":" + str(round(datas[0][k], 1)) + "\n"
        return result
    else:
        return

@register(name="Valuation Analysis", description="Get valuation analysis of company or industry", zh="估值分析")
def get_valuation_analysis(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    # print(name, entity_type, kwargs)
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        name = ENTITY.get_industry(name)
    if ENTITY.is_industry(name): 
        return industry_valuation(name)
    return "Valuation Analysis"


# 获取单只个股最新的估值指标
@register(name="Price/Earning Ratio", description="Get stock valuation by company", zh="估值指标")
@register(name="TTM Price/Earning", description="Get stock valuation by company")
@register(name="Price to Book Ratio", description="Get stock valuation by company")
def get_stock_value(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    # print(name, entity_type, kwargs)    
    if ENTITY.is_company_type(entity_type):
        return get_company_valuation(name)