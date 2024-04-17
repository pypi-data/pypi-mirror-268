import datetime
import numpy as np
import pandas as pd

from typing import (
    List,
    Any,
    Dict
)
from openfinance.datacenter.database.source.eastmoney.future import FutureSource

from openfinance.config import Config
from openfinance.strategy.feature.base import Feature
from openfinance.strategy.operator.base import OperatorManager

# 算法来源: http://www.sse.com.cn/assortment/options/neovolatility/c/4206989.pdf 
class Vix(Feature):
    name = "Vix"
    R  = 0.016
    
    def _user_source(
        self,
        name
    ):
        try:
            stock_name = "sh50"
            return FutureSource().get_future_data(stock_name)
        except:
            return None

    def eval(
        self,
        *args,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        data = kwargs.get("data", None)
        #stock_name = self.source.get("name", "sh50")
        #stock_name = kwargs.get("name", stock_name)
        return self.calcIvix(data)

    def caculateNearNextExpDate(
        self,
        data
    ):
        data = data
        data = data[data.days>7]
        #print(data)
        dates = data.sort_values("days")["days"].unique()
        #print(dates)
        return dates[0], dates[1]


    def caculateFK0(
        self,
        near_date,
        next_date,
        option
    ):   
        S1,gap1,S1_list = self.caculateMinGapStrike(near_date,option)
        S2,gap2,S2_list = self.caculateMinGapStrike(next_date,option)
        T1 = near_date/365.
        T2 = next_date/365.
        F1 = S1+np.exp(T1*self.R)*gap1
        F2 = S2+np.exp(T2*self.R)*gap2
        #K0为稍小于F并离F最近的可用执行价
        K01 = np.max([i for i in S1_list if i <=F1])
        K02 = np.max([i for i in S2_list if i <=F2])
        return F1,F2,K01,K02,T1,T2

    def caculateMinGapStrike(
        self,
        date,
        option
    ):
        """
            计算认购期权价格与认沽期权价格相差最小的执行价和对应的价差
            date: 到期日期
            return : 最小价差对应的执行价,最小价差,所有执行价构成的列表 
        """
        options = option
        option = options[(options['days']==date)]
        # option
        # print(option)
        option = pd.pivot_table(option,index='strike',columns='type',values='close')
        option['C_P'] = option['C'] - option['P']
        option['abs_gap'] = option['C_P'].abs()
        option = option.sort_values('abs_gap')
        atm_strike = option.index[0]
        min_gap = option['abs_gap'].values[0]
        return atm_strike,min_gap,option.index.tolist()

    def caculateSigma(
        self,
        date,
        K0,
        T,
        F,
        option
    ):
        options = option
        option = options[(options['days']==date)].copy()

        option.sort_values('strike',inplace=True)
        otm_put = option[(option['strike']<K0)&(option['type']=='P')]
        otm_call = option[(option['strike']>K0)&(option['type']=='C')]
        atm = option[option['strike']==K0]
        atm.loc[:, 'close'] = atm['close'].mean()
        atm.loc[:, 'type'] = 'mix'

        # 若  小于  ，为  对应的认沽期权价格；若  大于  ，为  对应的 
        #         认购期权价格；若  等于  ，为  对应的认沽期权价格与认购期权价格均值

        option = pd.concat([otm_put, atm.iloc[[0]], otm_call], ignore_index=True)
        option.sort_values('strike',inplace=True)
        option['delta_K'] = option['strike'].diff()
        option.iloc[0,-1] =option.iloc[1,-1]
        option['T'] = T
        option['R'] = self.R 
        option['var'] = option.apply(lambda x : (x['delta_K']/x['strike']**2)*np.exp(x['R']*x['T'])*x['close'],axis=1)
        var = option['var'].sum()
        sigma = (2/T)*var - (1/T)*(F/K0 - 1)**2
        return sigma

    def caculateIVX(
        self,
        sigma1,
        sigma2,
        T1, 
        T2, 
        NT1, 
        NT2
    ):
        ivx = None
        ivx = 100*((T1*sigma1*((NT2-30)/(NT2-NT1)) + T2*sigma2*((30-NT1)/(NT2-NT1)))*(365/30))**0.5
        return ivx

    def calcIvix(
        self,
        data
    ):
        #print(data)
        NT1, NT2 = self.caculateNearNextExpDate(data)
        #print(NT1, NT2)
        F1,F2,K01,K02,T1,T2 = self.caculateFK0(NT1, NT2, data)
        #print(F1,F2,K01,K02,T1,T2)
        sigma1 = self.caculateSigma(NT1,K01,T1,F1,data)
        #print(sigma1)
        sigma2 = self.caculateSigma(NT2,K02,T1,F1,data)
        #print(sigma2)
        ivx = self.caculateIVX(sigma1,sigma2,T1, T2, NT1, NT2)
        #print(ivx)
        return ivx