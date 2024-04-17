import pandas
import time
from typing import Any
from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager
from openfinance.datacenter.database.source.eastmoney.trade import stock_realtime
from openfinance.datacenter.database.storage.china.stock import trans_date
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.wrapper import wrapper
from openfinance.datacenter.echarts import ChartManager
from openfinance.datacenter.knowledge.entity_graph import EntityGraph, EntityEnum

db = DataBaseManager(Config()).get("db")

ENTITY = EntityGraph()

@register(name="Revenue Diversity", description="Get Revenue Diversity", zh="营收多元化")
@register(name="Value Proposition", description="Get Product or Value Proposition", zh="产品结构")
def get_product_proposition(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):
        columns_to_names = {
            "CATEGORY": "Product",
            "PERCENT_INCOME": "percentage of income (%)",
        }

        date = db.select_by_order(
            table = "t_main_business_f10 where SECURITY_NAME='" + name +"'",
            order_column = "DATE",
            limit_num = 2,
            field = "DATE"
        )[0]['DATE']

        data = db.select_more(
            table = "t_main_business_f10", 
            range_str = "SECURITY_NAME='" + name + "'and DIRECTION='按产品分' and DATE='" + date +"'",         
            field = ",".join(k for k, v in columns_to_names.items())
        )
        result = ""      
        if data:
            for i in range(len(data)):
                if data[i]["CATEGORY"] == "合计":
                    del data[i]
                    break
            result += "Income structure:\n"
            for d in data:
                result += d["CATEGORY"] + "(" + str(d["PERCENT_INCOME"]) + "%),"
            
            charts = ChartManager().get("pie")(
                data,
                {"x": "CATEGORY", "y": "PERCENT_INCOME", "title": "main business"}
                )
            return {"result": result, "chart": charts}
        return result
    return

@register(name="Revenue Streams", description="Get revenue stream of company", zh="收入明细")
def get_revenue_stream(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    return "Revenue Streams"

@register(name="Cost Structure", description="Get cost structure of company", zh="支出结构")
def get_cost_structure(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    columns_to_names = {
        "TOTAL_OPERATE_COST": "Total operate cost",
        "SALE_EXPENSE": "sales cost(%)",
        "MANAGE_EXPENSE": "management cost(%)",
        "OPERATE_EXPENSE": "operate cost(%)",
    }
    data = db.select_by_order(
        table = "t_income_profit_statement where SECURITY_NAME='"+ name + "'", 
        order_column = "DATE",
        limit_num = 6,            
        field = "DATE," + ",".join(k for k, v in columns_to_names.items())
    )
    result = "Cost Structure in temperal order:\n"
    for k, v in columns_to_names.items():
        if k != "TOTAL_OPERATE_COST":
            temp = v + ":"
            for d in data:
                if d[k]:
                    temp += str(round(100 * d[k]/d["TOTAL_OPERATE_COST"], 1)) + ","
            result += temp[:-1] + "\n"
    chart = ChartManager().get("multibar")(
        data,
        {"x": "DATE", "y": ["SALE_EXPENSE", "MANAGE_EXPENSE", "OPERATE_EXPENSE"], "title": "Cost Structure"}
        )
    return {"result": result, "chart": chart}

@register(name="Gross Profit Margin", description="Get gross profit margin of company", zh="毛利润分析")
def get_gross_profit_margin(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):  
        columns_to_names = {
            "GROSS_PROFIT_MARGIN": "gross profit margin(%)",
        }
        data = db.get_data_and_manuel_summary(
            table = "t_financial_report_statement where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            limit_num = 8,
            columns_to_names = columns_to_names,
            with_chart=True
        )
        data["chart"] = ChartManager().get("bar")(
            data["chart"], 
            {"x": "DATE", "y": "GROSS_PROFIT_MARGIN", "title": "Gross Profit Margin"}
        )
        return data
    return    

@register(name="Dividend Yield", description="Get Dividend Yield of company", zh="分红收益")
def get_divide(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):  
        data = db.select_by_order(
            table = "t_stock_divide where SECURITY_NAME='"+ name + "'", 
            order_column = "DATE",
            field = "DIVIDENT_PERCENT,DATE"        
        )
        if len(data):
            chart = ChartManager().get("bar")(
                data, 
                {"x": "DATE", "y": "DIVIDENT_PERCENT", "title": "Dividend Yield"}
            )
            #print(data)
            result = "Progressive Divident ratio(%): " + ", ".join(
                [str(round(d["DIVIDENT_PERCENT"] if d["DIVIDENT_PERCENT"] else 0, 2)) for d in data]
            )
            return {
                "result": result,
                "chart": chart
            }
        return "The company did not provide any divident"
    return

@register(name="Company Financials", description="Get company financial performance", zh="财务指标")
def get_financial_indicator(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):    
        columns_to_names = {    
            "YoY_REVENUE": "YoY Revenue(%)",
            "YoY_NET_PROFIT": "YoY net profit(%)",
            "RETURN_ON_NET_ASSET": "Return on net assets(%)",   
            "GROSS_PROFIT_MARGIN": "Gross profit margin(%)",
        }
        data = db.get_data_and_manuel_summary(
            table = "t_financial_report_statement where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            limit_num = 8,
            columns_to_names = columns_to_names,
            with_chart=True              
        )
        if "chart" in data:        
            data["chart"] = ChartManager().get("line")(
                data['chart'], 
                {"x": "DATE", "y": ["YoY_REVENUE", "YoY_NET_PROFIT"], "title": "Company Financials"}
            )
        return data
    elif ENTITY.is_industry(name):
        return 
    return 

@register(name="Debt to Equity Ratio", description="Get debt equity data of company", zh="资产负债比")
def get_company_debt_equity(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):      
        columns_to_names = {  
            "DEBT_ASSET_RATIO": "debt to asset ratio(%)",
        }
        data = db.get_data_and_manuel_summary(
            table = "t_balance_sheet_statement where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            limit_num = 6,        
            columns_to_names = columns_to_names,
            with_chart=True        
        )
        if "chart" in data:        
            data["chart"] = ChartManager().get("line")(
                data['chart'], 
                {"x": "DATE", "y": ["DEBT_ASSET_RATIO"], "title": "Debt to Equity Ratio"}
            )
        return data
    return


@register(name="Profitability", description="Get profit analysis of company", zh="盈利能力")
def get_profit_indicator(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):
        columns_to_names = {
            "YoY_OPERATE_PROFIT": "YoY of net profit of operation(%)",
            "YoY_DEDUCTED_NONPARENT_NET_PROFIT": "YoY of deducted nonparent net profit(%)",
        }
        data = db.get_data_and_manuel_summary(
            table = "t_income_profit_statement where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            limit_num = 6,
            columns_to_names = columns_to_names,
            with_chart=True        
        )
        if "chart" in data:        
            data['chart'] = ChartManager().get("line")(
                data['chart'], 
                {"x": "DATE", "y": ["YoY_OPERATE_PROFIT", "YoY_DEDUCTED_NONPARENT_NET_PROFIT"], "title": "Profitability"}
            )
        return data
    else:
        return

@register(name="Revenue Stability", description="Get Revenue Stability of company", zh="成长能力")
@register(name="Revenue Growth", description="Get Revenue Growth of company", zh="成长能力")
def get_grow_indicator(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):
        columns_to_names = {  
            "YoY_REVENUE": "YoY Revenue(%)",
            "SEQUENTIAL_REVENUE": "Quarter over Quarter Revenue(%)",
            "YoY_NET_PROFIT": "YoY net profit(%)",
            "SEQUENTIAL_NET_PROFIT": "Quarter over Quarter net profit(%)"
        }
        data = db.get_data_and_manuel_summary(
            table = "t_financial_report_statement where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            limit_num = 6,        
            columns_to_names = columns_to_names,
            with_chart=True               
        )
        if "chart" in data:        
            data['chart'] = ChartManager().get("line")(
                data['chart'], 
                {"x": "DATE", "y": ["YoY_REVENUE", "YoY_NET_PROFIT"], "title": "Revenue Growth"}
            )
        return data 
    return

@register(name="Cash Flow", description="Get Cash Flow of company", zh="现金流")
def get_cash_flow(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):  
        columns_to_names = {
            "YoY_NET_CASH_FLOW": "YoY net cash flow(%)",
            "YoY_OPERATING_NET_CASH_FLOW": "YoY cash flow from operation(%)"
        }
        data = db.get_data_and_manuel_summary(
            table = "t_cashflow_statement_dfcf where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            limit_num = 6,        
            columns_to_names = columns_to_names,
            with_chart=True         
        )
        if "chart" in data:        
            data['chart'] = ChartManager().get("line")(
                data['chart'], 
                {"x": "DATE", "y": ["YoY_NET_CASH_FLOW", "YoY_OPERATING_NET_CASH_FLOW"], "title": "Cash Flow"}
            )
        return data
    return  

@register(name="Stockholder Analysis", description="Get Stockholder Analysis of company", zh="股东情况")
def get_stockholder_analysis(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name): 
        columns_to_names = {
            "CAPITAL_PER_HOLDER": "Quarterly Capital per shareholder",
            "HOLDER_NUM_CHANGE": "Quarterly Holder's change",
        }
        data = db.get_data_and_manuel_summary(
            table = "t_stock_holder_num where SECURITY_NAME='"+ name + "'", 
            order_str = "DATE",
            columns_to_names = columns_to_names,    
            with_chart=True         
        )
        if "chart" in data:
            data['chart'] = ChartManager().get("bar")(
                data['chart'], 
                {"x": "DATE", "y": "HOLDER_NUM_CHANGE", "title": "Stockholder"}
            )
        return data
    return

@register(name="Forward Price/Earning", description="Get Forward Price/Earning of company", zh="远期市盈率")
def get_forward_pe(name="贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):
        try:
            price = stock_realtime(name)["最新"][0]
            res = db.select_one(
                table = "t_stock_eps_forecast",
                factor_str = "SECURITY_NAME='" + name + "'",
                field = "EPS2,EPS3"
            )
            #print(res)
            return f"""Forward Price/Earning is between {round(price/res.get("EPS2"), 1)} and {round(price/res.get("EPS3"), 1)}"""
        except:
            return ""
    return

@register(name="Sustainability", description="Get Sustainability of company", zh="发展可持续性")
@register(name="Growth Potential", description="Get Growth Potential of company", zh="业绩预估")
def get_forecast_predict(name= "贵州茅台", entity_type=EntityEnum.Company.type, **kwargs: Any):
    try:
        if entity_type == EntityEnum.Company.type and ENTITY.is_company(name):
            QDATE = db.select_by_order(
                table = "t_financial_report_statement where SECURITY_NAME='" + name + "'",
                order_column = "DATE",
                limit_num = 1,
                field = "DATE"
            )[0]['DATE']
            columns_to_names = {
                "PREDICT_FINANCE": "estimated indicator",
                "QUARTER_ON_QUARTER_LOWER": "forcast estimated quarter-on-quarter growth",
                "YoY_LOWER": "forcast estimated Year-on-year growth",
            }
            return db.get_data_and_manuel_summary(
                table = "t_stock_forcast_report where SECURITY_NAME='"+ name + "'and DATE >'" + QDATE + "'", 
                order_str = "PREDICT_FINANCE_CODE",
                columns_to_names = columns_to_names        
            )
        else:
            return
    except:
        return ""