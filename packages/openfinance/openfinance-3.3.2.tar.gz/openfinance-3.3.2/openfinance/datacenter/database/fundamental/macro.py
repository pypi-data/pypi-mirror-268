import pandas
import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.echarts import ChartManager
from openfinance.datacenter.database.wrapper import wrapper

db = DataBaseManager(Config()).get("db")

@register(name="Consumer confidence index", description="Get Consumer faith index", zh="消费者信心指数")
def get_consumer_faith(country= None, **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_consumer_faith", 
        order_str = "TIME",
        limit_num = 12,
        columns_to_names = {
            "TIME": "Month",            
            "FAITH_INDEX_SAME": "YoY FAITH_INDEX"
        },
        with_chart=True
    )
    data["chart"] = ChartManager().get("bar")(
        data["chart"], 
        {"x": "TIME", "y": "FAITH_INDEX_SAME", "title": "FAITH"}
    )
    return data

@register(name="GDP growth rate", description="Get GDP growth", zh="国内生产总值")
def get_gdp(country= None, **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_gdp", 
        order_str = "TIME",
        limit_num = 12,
        columns_to_names = {
            "TIME": "Season",
            "SUM_SAME": "YoY of Total GDP",
            "FIRST_SAME": "YoY of Primary Industry Production",
            "SECOND_SAME": "YoY of Secondary Industry Production",
            "THIRD_SAME": "YoY of Tertiary Industry Production"
        },
        with_chart=True
    )
    #print(data)
    #data["chart"] = ChartManager().get("bar")(data["chart"], {"x": "TIME", "y": "SUM_SAME", "title": "GDP"})
    data["chart"] = ChartManager().get("line")(
        data["chart"], 
        {"x": "TIME", "y": ["SUM_SAME", "FIRST_SAME", "SECOND_SAME", "THIRD_SAME"], "title": "GDP"}
    )
    return data

@register(name="Purchasing Manager Index", description="Get PMI index", zh="采购经理人指数")
def get_pmi(country= None, **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_pmi", 
        order_str = "TIME",
        limit_num = 5,        
        columns_to_names = {
            "TIME": "Month",
            "MAKE_INDEX": "Manufacturing PMI",
            "MAKE_SAME": "YoY of Manufacturing PMI",
            "NMAKE_INDEX": "Non-Manufacturing PMI",
            "NMAKE_SAME": "YoY of Non-Manufacturing PMI"
        },
        with_chart=True        
    )
    #data["chart"] = ChartManager().get("bar")(data["chart"], {"x": "TIME", "y": "MAKE_INDEX", "title": "PMI"})
    data["chart"] = ChartManager().get("line")(
        data["chart"], 
        {"x": "TIME", "y": ["MAKE_INDEX", "NMAKE_INDEX"], "title": "PMI"}
        )
    return data

@register(name="Producer Price Index", description="Get Purchasing Managers Index", zh="生产者物价指数")
def get_ppi(country= None, **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_ppi", 
        order_str = "TIME",
        limit_num = 5,        
        columns_to_names = {
            "TIME": "Month",            
            "BASE": "PPI",
            "BASE_SAME": "YoY of PPI"
        },
        with_chart=True        
    )
    data["chart"] = ChartManager().get("bar")(
        data["chart"], 
        {"x": "TIME", "y": "BASE", "title": "PMI"}
    )
    return data

@register(name="Interest Rates", description="Get lpr (Loan Prime Rate)", zh="贷款基准利率")
def get_lpr(country= None, **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_lpr", 
        order_str = "TIME",
        limit_num = 5,        
        columns_to_names = {
            "TIME": "Month",
            "RATE_1": "1 Year Loan Rate",
            "RATE_2": "5 Year Loan Rate"
        },
        with_chart=True        
    )
    data["chart"] = ChartManager().get("bar")(
        data["chart"], 
        {"x": "TIME", "y": "RATE_2", "title": "LPR5"}
        )
    return data

@register(name="Money Supply", description="Get Money Supply", zh="货币供应量")
def get_money_supply(country= None, **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_money_supply", 
        order_str = "TIME",
        limit_num = 5,        
        columns_to_names = {
            "TIME": "Month",
            "BASIC_CURRENCY_SAME": "YoY of Base Currency",
            "FREE_CASH_SAME": "YoY of Circulating Currency"
        },
        with_chart=True        
    )
    data["chart"] = ChartManager().get("bar")(
        data["chart"], 
        {"x": "TIME", "y": "BASIC_CURRENCY_SAME", "title": "Money Supply"}
    )
    return data    

@register(name="Inflation Rate", description="Get Inflation Rate", zh="通货膨胀率")
def get_inflation_rate(country=None, **kwargs: Any):
    return "Inflation Rate"

@register(name="Consumer Price Index", description="Get CPI index", zh="消费者物价指数")
def get_cpi(country= None, **kwargs: Any): 
    data = db.get_data_and_manuel_summary(
        table = "t_macro_cpi", 
        order_str = "TIME",
        limit_num = 5,        
        columns_to_names = {
            "TIME": "Month",
            "NATIONAL_SAME": "YoY of CPI",
            "NATIONAL_SAME": "Sequential of CPI"
        },
        with_chart=True        
    )
    data["chart"] = ChartManager().get("bar")(
        data["chart"], 
        {"x": "TIME", "y": "NATIONAL_SAME", "title": "CPI"}
    )
    return data    

@register(name="Macro Economic", description="Get Macro Economy Indicator", zh="宏观经济数据")
def get_main_macro(county="CHINA", **kwargs: Any):
    return "Macro Economic"

@register(name="Bond Yield", description="Get treasury Bond Yield", zh="国债收益率")
def get_bond_yield(country="US", **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_treasury_bond_yield", 
        order_str = "DATE",
        limit_num = 360,        
        columns_to_names = {
            "DATE": "date",
            "CNY10Y": "10 Years of China treasury bond rate",            
            "US10Y": "10 Years of US treasury bond rate",
            "US10Y_2Y": "Difference about 10 Years bond minus 2 Years bond"
        },
        with_chart=True
    )
    data["chart"] = ChartManager().get("line")(
        data["chart"], 
        {"x": "DATE", "y": ["US10Y", "CNY10Y", "US10Y_2Y"], "title": "Bond Yield"}
    )
    return data

@register(name="External Factors", description="Get External Factors", zh="外部国际因素")
def get_external_factors(country="China", **kwargs: Any):
    return "External Factors"

@register(name="International Trade", description="Get International Trade Data", zh="国际贸易进出口")
def get_international_trade(country="China", **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_macro_international_trade", 
        order_str = "TIME",
        limit_num = 12,        
        columns_to_names = {
            "TIME": "Month",
            "EXPORT_BASE_YoY": "YoY ratio of export volume (dollars)",            
            "IMPORT_BASE_YoY": "YoY ratio of import volume (dollars)",
        },
        with_chart=True
    )
    data["chart"] = ChartManager().get("line")(
        data["chart"], 
        {"x": "TIME", "y": ["EXPORT_BASE_YoY", "IMPORT_BASE_YoY"], "title": "International Trade"}
    )
    return data



@register(name="Center Bank Balance Sheet", description="Get Center Bank balance sheet", zh="中央银行资产负债表")
def get_center_bank_balance_sheet(country="US", **kwargs: Any):
    data = db.get_data_and_manuel_summary(
        table = "t_us_fred_balance_sheet", 
        order_str = "DATE",
        limit_num = 50,        
        columns_to_names = {
            "DATE": "date",
            "CHANGE_WEEKLY": "week over week change in lastest week",
            "CHANGE_YEAR": "Year over year change in lastest week"
        },
        with_chart=True
    )
    #print(data)
    data["chart"] = ChartManager().get("bar")(
        data["chart"], 
        {"x": "DATE", "y": "CHANGE_WEEKLY", "title": "FED Balance Sheet"}
    )
    return data    

@register(name="Fiscal Policy", description="Get Fiscal Policy", zh="财政政策")
@register(name="Government Revenue Debt", description="Get Government Revenue Debt", zh="政府应收支出")
@register(name="Budget deficit or surplus", description="Get Budget deficit or surplus", zh="财政预算")
def get_fiscal_policy(country="US", **kwargs: Any):
    if country == "US":
        data = db.get_data_and_manuel_summary(
            table = "t_us_us_government_fiscal", 
            order_str = "DATE",
            limit_num = 3,        
            columns_to_names = {
                "DATE": "date",
                "Total_Receipts": "Total Receipts",
                "Total_Receipts_Last_Year": "Total Receipts Last Year",
                "Total_Outlays": "Total Outlays",
                "Total_Outlays_Last_Year": "Total Outlays Last Year"
            },
            with_chart=True
        )
        data["chart"] = ChartManager().get("line")(
            data["chart"],
            {
                "x": "DATE", 
                "y": ["Total_Receipts", "Total_Receipts_Last_Year", "Total_Outlays", "Total_Outlays_Last_Year"], 
                "title": "FED Balance Sheet"
            }
        )
        return data
    else: # chinese
        hidden_debt = get_macro_risk()
        govern_debt = db.get_data_and_manuel_summary(
            table = "t_china_government_debt", 
            order_str = "TIME",
            limit_num = 2,        
            columns_to_names = {
                "TIME": "Year",
                "FiscalIncome": "Fiscal income",
                "FiscalCost": "Fiscal cost",
                "NationalDebt": "Country total bond"
            }
        )
        local_debt = db.get_data_and_manuel_summary(
            table = "t_china_local_government_debt", 
            order_str = "TIME",
            limit_num = 10,        
            columns_to_names = {
                "TIME": "Month",
                "LOCAL_GOV_BOND": "local government bond"
            },
            with_chart=True
        )
        local_debt["chart"] = ChartManager().get("bar")(
            local_debt["chart"], 
            {"x": "TIME", "y": "LOCAL_GOV_BOND", "title": "LOCAL_GOV_BOND"}
        )        
        return wrapper([
            hidden_debt,
            govern_debt,
            local_debt
        ])

def get_macro_risk(country="CHINA", **kwargs: Any):
    """## chinese: 获取宏观风险
    ## english: Get macro risk
    ## args:
    ## extra:
    """
    return "The hidden local government debt is quite high and the center government is solving it"