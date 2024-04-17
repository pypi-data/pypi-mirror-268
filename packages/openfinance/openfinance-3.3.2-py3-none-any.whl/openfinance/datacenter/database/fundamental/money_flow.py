import pandas
import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.echarts import ChartManager
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum
from openfinance.datacenter.database.source.eastmoney.market import (
    north_money_flow,
)
from openfinance.datacenter.database.quant.call import get_factor_process

db = DataBaseManager(Config()).get("db")
ENTITY = EntityGraph()

def get_company_money_flow(name):
    try:
        columns_to_names = {
            "CAPITAL_FLOWS": "daily money flow of company",
            "BOARD_CAPITAL_FLOWS": "daily money flow of sector",
        }
        #print(columns_to_names)      
        data = db.get_data_and_manuel_summary(
            table = "t_stock_money_flow where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            columns_to_names = columns_to_names,
            with_chart=True
        )
        data['chart'] = ChartManager().get("bar")(
            data['chart'], 
            {"x": "DATE", "y": "CAPITAL_FLOWS", "title": "Money Flow"}
        )
        return data
    except Exception as e:
        print(e)
        return 

def get_industry_money_flow(name):
    datas = db.select_more(
        table = "t_industry_north_money_to_sector",
        range_str = "INDUSTRY_NAME='" + name + "'"
    )
    result = ""
    columns = {
        "1": "daily foreign money inflow / market value ratio (%)",
        "5": "weekly foreign money inflow / market value ratio (%)",
        "M": "monthly foreign money inflow / market value ratio (%)"
    }
    for d in datas:
        if d["INTERVAL_TYPE"] in columns:
            result += columns[d["INTERVAL_TYPE"]] + ":" + str(round(d["MARKET_CAPITAL_INCOME_RATIO"], 1)) + "\n"
    return result

@register(name="Money Flow", description="Get Money Flow of company", zh="个股每天资金流动情况")
def get_money_flow(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        name = ENTITY.get_industry(name)
    if ENTITY.is_industry(name):
        return get_industry_money_flow(name)
    return get_company_money_flow(name)        


@register(name="Market Foreign Money Flow", description="Get market foreign money flow", zh="市场外资流入流出")
def get_foreign_money_flow(name="沪深300", **kwargs: Any):
    """Get market foreign money flow
    Args:
        code: stock name 
    Returns:
        The string required for llm
    """
    data = north_money_flow()
    data['MA'] = get_factor_process("MovingAverage", data['VOLUME'])
    data['MACD'] = get_factor_process("MACD", data['VOLUME'])
    chart = ChartManager().get("line")(
        data,
        {"x": "DATE", "y": ["MA", "MACD"], "title": "Foreign Money Flow"}
    )
    msg = "Movering Average of foreign money flow is " + str(data['MA'][-5:])
    result = {
        "result": msg,
        "chart": chart
    }
    return result