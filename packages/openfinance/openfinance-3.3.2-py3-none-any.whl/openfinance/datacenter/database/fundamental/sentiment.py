import pandas
import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.echarts import ChartManager
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

from openfinance.datacenter.database.fundamental.money_flow import (
    get_money_flow,
    get_foreign_money_flow
)
from openfinance.datacenter.database.fundamental.volume import get_market_volume
from openfinance.datacenter.database.fundamental.financial import get_stockholder_analysis

ENTITY = EntityGraph()
db = DataBaseManager(Config()).get("db")

@register(name="Sentiment Analysis", description="Get Sentiment Analysis of company", zh="情绪分析")
def get_sentiment_analysis(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    return "Sentiment Analysis"

@register(name="Market Sentiment", description="Get Market Sentiment", zh="市场情绪")
def get_market_sentiment(name="", entity_type=EntityEnum.Market.type, **kwargs: Any):
    return "Market Sentiment"

@register(name="Market Financing Balance", description="Get Stock Market Financing Balance", zh="市场融资融券")
def get_market_financing_balance(name="", entity_type="country", **kwargs: Any):
    if ENTITY.is_company_type(entity_type):
        return
    if ENTITY.is_industry_type(entity_type):
        return
    data = db.get_data_and_manuel_summary(
        table = "t_market_loan_money", 
        order_str = "DATE",
        limit_num = 100,
        columns_to_names = {
            "DATE": "DATE",            
            "Financing_Balance": "Financing Balance",
            "Financing_Purchase_Amount": "Financing Purchase Amount",
            "Margin_Trading_Balance": "Margin_Trading_Balance",
            "Margin_Trading_Balance_Amount": "Margin_Trading_Balance_Amount"
        },
        with_chart=True
    )
    data["chart"] = ChartManager().get("line")(
        data["chart"], 
        {
            "x": "DATE", 
            "y": [
                "Financing_Balance", 
                "Financing_Purchase_Amount", 
                "Margin_Trading_Balance", 
                "Margin_Trading_Balance_Amount"
            ], 
            "title": "Market Financing Balance"}
    )
    return data

@register(name="Social Media Index", description="Get Social Media Index", zh="关注指数")
def get_social_index(name="", entity_type=EntityEnum.Company.type, **kwargs: Any):
    # to do calc news docs
    return 

