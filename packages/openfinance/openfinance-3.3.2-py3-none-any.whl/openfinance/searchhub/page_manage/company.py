import json
from typing import Any, Dict, List
from openfinance.searchhub.page_manage.base import BaseElement
from openfinance.datacenter.database.source.eastmoney.trade import stock_billboard
from openfinance.datacenter.database.base import DataBaseManager

class Company(BaseElement):
    stype: str = "Company"

class CompanyManager:

    def __init__(
        self,
        config
    ):
        self.db = DataBaseManager(config).get("db")
        self.type_to_ele: Dict[str, Company] = {}

    def register(
        self, 
        name: str, 
        base: Company
    ) -> None:
        if name not in self.type_to_ele:
            self.type_to_ele[name] = base

    def get(
        self, 
        name: str
    ) -> Company:
        return self.type_to_ele.get(name, None)

    # will be moved to db later
    def get_details(
        self, 
        company: str
    ) -> Dict[str, Any]:
        return {
            "company": company,
            "icon": "",
            "id": "",
        }

    def get_homepage(
        self, 
        num: int
    ) -> Dict[str, Any]:
        result = []
        data = stock_billboard()['股票名称'].to_list()
        for d in data:
            result.append(self.get_details(d))
        #print(result)
        return result

    def search(
        self,
        text: str,
        num: int
    ) -> Dict[str, Any]:
        result = []
        print("text", text)
        try:
            data = self.db.select_more(
                table = "t_balance_sheet_statement",
                range_str = f"SECURITY_NAME like '%{text}%'",
                field = "distinct(SECURITY_NAME)",
            )
        except Exception as e:
            print(e)
        print("data", data)
        for d in data:
            result.append(self.get_details(d['SECURITY_NAME']))
        return result

