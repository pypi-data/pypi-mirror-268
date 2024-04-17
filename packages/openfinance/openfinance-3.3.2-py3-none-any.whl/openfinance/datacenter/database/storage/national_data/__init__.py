from openfinance.datacenter.database.storage.financial import (
    store_main_business,
    store_stock_holder,
    store_cash_flow,
    store_financial_report_statement,
    store_income_profit,
    store_balance_sheet,
    store_forcast_report,
    store_eps_forecast,
    store_stock_divide,
    store_money_flow
)
from openfinance.datacenter.database.storage.industry import (
    store_north_money_to_sector
)

from openfinance.datacenter.database.storage.macro import (
    build_marco
)

from openfinance.datacenter.database.storage.fred.store import (
    build_fed
)

stock_func = [
    store_main_business,
    store_stock_holder,
    store_cash_flow,
    store_financial_report_statement,
    store_income_profit,
    store_balance_sheet,
    store_forcast_report,
    store_eps_forecast,
    store_stock_divide,
    store_money_flow,
    build_marco,
    build_fed,
    store_north_money_to_sector
]