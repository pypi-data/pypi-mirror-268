"""
Created on Fri Sep 30 13:53:48 2022

"""
import time
import requests
import calendar
import pandas as pd
from datetime import datetime
from jsonpath import jsonpath
from tqdm import tqdm
from bs4 import BeautifulSoup

from openfinance.datacenter.database.source.eastmoney.trade import (
    market_realtime
)
from openfinance.datacenter.database.source.eastmoney.util import (
    latest_report_date,    
    trans_num,
    get_code_id,
    request_header, 
    session,
    trans_date
)

def get_key():
    url = "https://datacenter.eastmoney.com/securities/api/data/v1/get"  
    params = {  
        'reportName': 'RPT_USF10_FN_BALANCE',  
        'columns': 'SECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,STD_ITEM_CODE,ITEM_NAME',  
        'quoteColumns': '',  
        'filter': '(SECUCODE="TSLA.O")',  
        'distinct': 'STD_ITEM_CODE',  
        'pageNumber': '',  
        'pageSize': '',  
        'sortTypes': '1,-1',  
        'sortColumns': 'STD_ITEM_CODE,REPORT_DATE',  
        'source': 'SECURITIES',  
        'client': 'PC',  
        'v': '02026439087156524'  
    }  
   
    res = requests.get(url, params=params)
    data_json = res.json()
    id_to_name = {}
    for d in data_json["result"]["data"]:
        id_to_name[d["STD_ITEM_CODE"]] = d["ITEM_NAME"]
    return id_to_name

name_to_key = {
    '004001001': 'cash_and_cash_equivalents',
    '004001002': 'restricted_cash_and_others_(current)',
    '004001003': 'short_term_investments',
    '004001004': 'accounts_receivable',
    '004001008': 'inventory',
    '004001009': 'deferred_tax_assets_(current)',
    '004001013': 'prepaid_expenses_(current)',
    '004001014': 'other_current_assets',
    '004001016': 'securities_investment_(current)',
    '004001999': 'total_current_assets',
    '004003001': 'property_plant_and_equipment',
    '004003002': 'fixed_assets',
    '004003003': 'intangible_assets',
    '004003004': 'goodwill',
    '004003006': 'restricted_cash_and_others_(non_current)',
    '004003007': 'long_term_investments',
    '004003009': 'deferred_tax_assets_(non_current)',
    '004003014': 'other_non_current_assets',
    '004003018': 'other_long_term_receivables',
    '004003097': 'non_current_assets_other_items',
    '004003999': 'total_non_current_assets',
    '004005999': 'total_assets',
    '004007001': 'accounts_payable',
    '004007003': 'notes_payable_(current)',
    '004007004': 'taxes_payable_(current)',
    '004007005': 'unearned_revenues_and_accrued_expenses',
    '004007007': 'short_term_debt',
    '004007008': 'long_term_liabilities_(current_portion)',
    '004007010': 'deferred_revenue_(current)',
    '004007012': 'other_current_liabilities',
    '004007013': 'customer_deposits_and_advances',
    '004007015': 'capital_lease_liabilities_(current)',
    '004007097': 'current_liabilities_other_items',
    '004007999': 'total_current_liabilities',
    '004009001': 'deferred_tax_liabilities_(non_current)',
    '004009002': 'deferred_revenue_(non_current)',
    '004009005': 'long_term_liabilities',
    '004009006': 'convertible_notes_and_bonds',
    '004009007': 'other_non_current_liabilities',
    '004009008': 'payables_to_related_parties_(non_current)',
    '004009010': 'derivative_instrument_liabilities_(non_current)',
    '004009011': 'capital_lease_liabilities_(non_current)', 
    '004009097': 'non_current_liabilities_other_items', 
    '004009999': 'total_non_current_liabilities', 
    '004011999': 'total_liabilities', 
    '004013001': 'common_stock', 
    '004013002': 'preferred_stock', 
    '004013003': 'treasury_stock', 
    '004013004': 'retained_earnings', 
    '004013006': 'capital_surplus', 
    '004013007': 'other_comprehensive_income', 
    '004013097': 'parent_company_equity_other_items', 
    '004013999': 'parent_company_equity', 
    '004015999': 'minority_interest', 
    '004017097': 'equity_total_other_items', 
    '004017999': 'equity_total', 
    '004021999': 'liabilities_and_equity_total', 
    '004023999': 'non_operating_items'
}