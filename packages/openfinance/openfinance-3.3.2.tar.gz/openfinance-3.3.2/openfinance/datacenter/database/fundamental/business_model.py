import pandas
import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager

from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.echarts import ChartManager

from openfinance.datacenter.database.fundamental.financial import (
    get_product_proposition,
    get_cost_structure,
    get_forecast_predict
)
from openfinance.datacenter.database.fundamental.competitiveness import (
    get_brand_strength
)


db = DataBaseManager(Config()).get("db")

@register(name="Business Model", description="Get business model of company", zh="主要业务")
def get_business_model(name= "贵州茅台", **kwargs: Any):
    return "Business Model"