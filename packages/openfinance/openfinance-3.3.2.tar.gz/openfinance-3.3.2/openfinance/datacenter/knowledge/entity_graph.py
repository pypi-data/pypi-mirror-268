from typing import Any, Dict, List, Optional, Set
from dataclasses import dataclass
from enum import Enum

from openfinance.utils.singleton import singleton

from openfinance.config import Config
from openfinance.datacenter.database.base import DataBaseManager


class EntityEnum(Enum):
    """实体枚举类"""

    Company = ("Company", "公司")
    Industry = ("Industry", "行业")
    Market = ("Market", "市场")
    Economy = ("Economy", "宏观")

    @property
    def type(self):
        """获取英文类型"""
        return self.value[0]

@dataclass
class Company:
    name: str
    code_id: str
    industries: List[str]

@dataclass
class Industry:
    name: str
    code_id: str
    companies: List[str]

@singleton
class EntityGraph:
    def __init__(
        self
    ):
        self.conf = Config()
        self.db = DataBaseManager(self.conf).get("db")
        self._init_type()
        self._add_companies()
        self._add_industries()

    def _init_type(
        self
    ):
        self.entity_type = [
           EntityEnum.Company.type,
           EntityEnum.Industry.type,
           EntityEnum.Market.type,
           EntityEnum.Economy.type
        ]
        self.factor_to_entity_type = {
            "Company Analysis": EntityEnum.Company.type,
            "Industry Analysis": EntityEnum.Industry.type,
            "Market Analysis": EntityEnum.Market.type,
            "Macro Economic": EntityEnum.Economy.type
        }

    def get_types(
        self
    ):
        return self.entity_type

    def _add_companies(
        self
    ):
        self.companies = {}
        try:
            sql = "select distinct(SECURITY_NAME), SECURITY_CODE, INDUSTRY_NAME from t_balance_sheet_statement"
            data = self.db.exec(sql)
            for d in data:
                #print(d)
                self.companies[d['SECURITY_NAME']] = Company(
                    name = d['SECURITY_NAME'],
                    code_id = d['SECURITY_CODE'],
                    industries = [d['INDUSTRY_NAME']]
                )
        except Exception as e:
            print(e)

    def _add_industries(
        self
    ):
        self.industries = {}
        try:
            sql = "select distinct(SECURITY_NAME), INDUSTRY_NAME from t_balance_sheet_statement"
            data = self.db.exec(sql)
            for d in data:
                if d["INDUSTRY_NAME"] in self.industries:
                    self.industries[d["INDUSTRY_NAME"]].append(d["SECURITY_NAME"])
                else:
                    self.industries[d["INDUSTRY_NAME"]] = [d["SECURITY_NAME"]]
        except Exception as e:
            print(e)

    def is_company_type(
        self,
        text
    ) -> bool:
        if text == EntityEnum.Company.type:
            return True
        return False

    def is_industry_type(
        self,
        text
    ) -> bool:
        if text == EntityEnum.Industry.type:
            return True
        return False

    def is_market_type(
        self,
        text
    ) -> bool:
        if text == EntityEnum.Market.type:
            return True
        return False

    def is_economy_type(
        self,
        text
    ) -> bool:
        if text == EntityEnum.Economy.type:
            return True
        return False

    def is_company(
        self,
        text
    ) -> bool:
        if text in self.companies:
            return True
        return False
    
    def is_industry(
        self,
        text
    ) -> bool:
        if text in self.industries:
            return True
        return False

    #  right now only consider one industry, update later
    def get_industry_company(
        self,
        industry
    ) -> str:
        return self.industries.get(industry, [])

    #  right now only consider one industry, update later
    def get_industry(
        self,
        company
    ) -> str:
        if company in self.companies:
            industries = self.companies.get(company).industries
            if len(industries):
                return industries[0]
        return ""
    
    def get_type_from_graph_path(
        self,
        paths
    ):
        """Used while graph factor call"""
        for path in paths:
            if path in self.factor_to_entity_type:
                return self.factor_to_entity_type[path]

    def extract_entity(
        self,
        text: str,
    ) -> str:
        for k, v in self.companies.items():
            if k in text:
                return k
        for k in self.industries:
            if k in text:
                return k
        if "A股" in text:
            return "A股"
        return ""