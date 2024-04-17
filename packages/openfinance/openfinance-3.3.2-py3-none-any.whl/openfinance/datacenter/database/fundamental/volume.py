from typing import Any

from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.echarts import ChartManager
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

from openfinance.datacenter.database.quant.call import get_factor_process
from openfinance.datacenter.database.source.eastmoney.trade import quant_data
from openfinance.datacenter.database.source.eastmoney.technical import get_price_volume_status

ENTITY = EntityGraph()

@register(name="Volume Analysis", description="Get volume analysis of Company", zh="量价分析")
def get_volume_analysis(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if ENTITY.is_company(name) and ENTITY.is_industry_type(entity_type):
        name = ENTITY.get_industry(name)
    elif entity_type == EntityEnum.Market.type:
        return "Volume Analysis"
    if ENTITY.is_industry(name):  # to add later
        return 
    return get_price_volume_status(name)

@register(name="Market Volume", description="Get Market Money Volume Analysis", zh="市场资金流动")
def get_market_volume(name="China", entity_type=EntityEnum.Company.type, **kwargs: Any):
    """Get stock market volume.
    Args:
        code: stock name    
    Returns:
        The string required for llm
    """

    Big_Company_Volume_Monthly = (quant_data("399300", freq='m', fqt=2)['volume'][-100:]/100000000).round(1).tolist()
    Small_Company_Volume_Monthly = (quant_data("399905", freq='m', fqt=2)['volume'][-100:]/100000000).round(1).tolist()

    Big_Company_Volume_Weekly = (quant_data("399300", freq='w', fqt=2)['volume'][-100:]/100000000).round(1).tolist()
    Small_Company_Volume_Weekly = (quant_data("399905", freq='w', fqt=2)['volume'][-100:]/100000000).round(1).tolist()

    data = {
        "DATE": [i for i in range(100)],
        "MACD of Monthly Trading Volume": get_factor_process("MACD", Big_Company_Volume_Monthly),
        "MACD of Monthly Trading Volume Small Company": get_factor_process("MACD", Small_Company_Volume_Monthly),
        "MACD of Weekly Trading Volume": get_factor_process("MACD", Big_Company_Volume_Weekly),
        "MACD of Weekly Trading Volume Small Company": get_factor_process("MACD", Small_Company_Volume_Weekly)
    }

    chart = ChartManager().get("line")(
        data,
        {"x": "DATE", "y": [
            "MACD of Monthly Trading Volume", 
            "MACD of Monthly Trading Volume Small Company",
            "MACD of Weekly Trading Volume",
            "MACD of Weekly Trading Volume Small Company"
            ], "title": "Big/Small Company Weekly/Monthly Volume MACD"}
    )
    data.pop("DATE")
    msg = "\n".join([k + ": "+ str(v[-5:]) for k, v in data.items()])
    result = {
        "result": msg,
        "chart": chart
    }
    return result