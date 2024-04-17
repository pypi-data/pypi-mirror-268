from typing import Any

from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.knowledge.entity_graph import (
    EntityGraph,
    EntityEnum
)

ENTITY = EntityGraph()
@register(name="Technical Analysis", description="Get technical analysis of stcok", zh="量价技术分析")
def get_technical_analysis(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        name = ENTITY.get_industry(name)
    if ENTITY.is_industry(name):  # to add later
        return 
    return "Technical Analysis"


@register(name="Price Trends", description="Get price trend analysis", zh="价格趋势分析")
def get_price_trends(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        name = ENTITY.get_industry(name)
    if ENTITY.is_industry(name):  # to add later
        return
    return "Price Trend"