import pandas
import time
from typing import Any

from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.echarts import ChartManager

from openfinance.datacenter.database.quant.call import get_factor_process
from openfinance.datacenter.database.source.eastmoney.trade import quant_data
from openfinance.datacenter.database.fundamental.volume import get_market_volume
from openfinance.datacenter.database.fundamental.money_flow import get_foreign_money_flow
from openfinance.datacenter.database.fundamental.sentiment import get_market_sentiment

@register(name="Market Analysis", description="Get market trend analysis", zh="市场趋势")
def get_market_analysis(name="沪深300", entity_type="Market", **kwargs: Any):
    """Get stock market trend.
    Args:
        code: stock name    
    Returns:
        The string required for llm
    """
    return "Market Analysis"

@register(name="Overall Market Performance", description="Get overall market performance position", zh="市场整体表现")
def get_overall_market_performance(name="沪深300", entity_type="Market", **kwargs: Any):
    """Get Overall Market Performance
    Args:
        code: stock name    
    Returns:
        The string required for llm
    """
    Big_Company_Volume_Monthly = (quant_data("399300", freq='m', fqt=2)['close'][-100:]).tolist()
    Big_Company_Volume_Weekly = (quant_data("399300", freq='w', fqt=2)['close'][-100:]).tolist()
    Big_Company_Volume_Daily = (quant_data("399300", freq='d', fqt=2)['close'][-100:]).tolist()


    data = {
        "DATE": [i for i in range(100)],
        "Monthly MACD of Market Index": get_factor_process("MACD", Big_Company_Volume_Monthly),
        "Weekly MACD of Market Index": get_factor_process("MACD", Big_Company_Volume_Weekly),
        "Daily MACD of Market Index": get_factor_process("MACD", Big_Company_Volume_Daily),
    }

    chart = ChartManager().get("line")(
        data,
        {"x": "DATE", "y": [
            "Monthly MACD of Market Index", 
            "Weekly MACD of Market Index",
            "Daily MACD of Market Index"            
            ], "title": "Market Index MACD"
        }
    )
    data.pop("DATE")
    msg = "\n".join([k + ": "+ str(v[-5:]) for k, v in data.items()])
    result = {
        "result": msg,
        "chart": chart
    }
    return result
