import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.echarts import ChartManager
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

from openfinance.datacenter.database.fundamental.valuation import get_valuation_analysis
from openfinance.datacenter.database.fundamental.business_model import get_business_model
from openfinance.datacenter.database.fundamental.financial import get_financial_indicator

ENTITY = EntityGraph()

@register(name="Fundamental Analysis", description="Get fundamental analysis of company", zh="基本面分析")
def get_fundamental_analysis(name="贵州茅台", **kwargs: Any):
    return "Fundamental Analysis"