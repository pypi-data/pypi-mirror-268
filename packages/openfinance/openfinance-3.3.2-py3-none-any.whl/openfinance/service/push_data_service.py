# -*- coding: utf-8 -*-
# (C) Run, Inc. 2022
# All rights reserved (Author BinZHU)
# Licensed under Simplified BSD License (see LICENSE)

import os
import sys
import time
import datetime
import argparse
import inspect
import threading

from flask import Flask, request, jsonify
from flask_cors import CORS

from openfinance.utils.log import get_logger
from openfinance.service.error import StatusCodeEnum
from openfinance.service.auth.login import LoginManager

from openfinance.strategy.policy.market_danger import MarketDanger
from openfinance.strategy.policy.market_sentiment import MarketSentiment
from openfinance.strategy.policy.company_ranker import CompanyIndexSort

from openfinance.datacenter.database.source.event.jin10 import (
    get_economic,
    get_event
)
from openfinance.strategy.feature.base import FeatureManager

from openfinance.service.base import wrapper_return

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
CORS(app, resources=r'/*')

logger = get_logger("homepage.log")
login_manager = LoginManager("accounts")
NAME = "上证指数"

market_danger = MarketDanger.from_file()
market_sentiment = MarketSentiment.from_file()
company_ranker = CompanyIndexSort.from_file()

@app.route('/', methods = ['GET', 'POST'])
def connect():
    logger.info("recieve request")
    ret = jsonify(message = "Congrats! Connected!", status = StatusCodeEnum.OK.code)
    logger.info('output: {}'.format(ret.data.decode('utf8')))
    return ret

@app.route('/api/register', methods=['POST'])
def register():

    data = request.get_json(force=True)
    logger.info('data: {}'.format(data))

    user = data['data']['user']
    passwd = data['data']['passwd']
    err = login_manager.register(user, passwd)
    logger.info(f"register: {user}, {err.msg}")
    return jsonify(msg = err.msg, ret_code = err.code)

def login(request):
    user = request['header']['user']
    req_id = request['header']['req_id']
    token = request['header']['token']
    return login_manager.login_with_token(user, req_id, token)


@app.route('/api/strategy/sentiment', methods=['GET'])
def sentiment():
    try:
        senti = market_sentiment.run(
            candidates = [NAME],
            from_db=True,
            type="market",
            latest=True     
        )
        features = market_sentiment.features(
            candidates=[NAME],
            from_db=True,        
            type="market"
        )
        for name in list(features.keys()):
            features[FeatureManager().get(name).desc] = features.pop(name)
        result = {
            "summary": senti,
            "features": features
        }
        ret = jsonify ( result = result,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)        
    except Exception as e:
        print(e)
        ret = jsonify ( result = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

@app.route('/api/strategy/danger', methods=['GET'])
def danger(): 
    try:
        senti = market_danger.run(
            candidates = [NAME],
            from_db=True,
            type="market",
            latest=True     
        )
        features = market_danger.features(
            candidates=[NAME],
            from_db=True,        
            type="market"
        )
        for name in list(features.keys()):
            features[FeatureManager().get(name).desc] = features.pop(name)
        result = {
            "summary": senti,
            "features": features
        }
        ret = jsonify ( result = result,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)            
    except:
        ret = jsonify (models = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

@app.route('/api/strategy/stock', methods=['GET'])
def stock():   
    try:
        stocks = company_ranker.run(
            reverse = {
                "OperationGrow": True,
                "ProfitGrow": True,
                "GrossProfit": True,
                "ProfitSpeedAcc": True,
                "OperationSpeedAcc": True,
                "NetProfitRatio": True,
                "ROE": True,
                "DividentSpeed": True,
                "DividentMean": True,
                "GrossProfitYoY": True,
                "FreeCashFlowYield": True,
                "NetCashFlowYoY": True,
                "FreeCashRatio": True,
                "WinCostDist": True,
                "MoneyFlowDirect": True
            },
            negative = {
                "PriceEarning": True
            },
            from_db=True,
            type="company"
        )

        features = company_ranker.features(
            candidates= list(stocks.keys()),
            from_db=True,
            type="company"
        )

        for name in list(features.keys()):
            features[FeatureManager().get(name).desc] = features.pop(name)

        result = {
            "summary": stocks,
            "features": features
        }
        # print(result)
        ret = jsonify ( result = result,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)          
    except Exception as e:
        print(e)
        ret = jsonify (models = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

@app.route('/api/strategy/event', methods=['GET'])
def event():   
    try:
        data = {
            "economic": get_economic(),
            "event": get_event(),
            "future_economic": {},
            "future_event": {}
        }
        ret = jsonify ( data = data,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)    
    except Exception as e:
        print(e)
        ret = jsonify ( data = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    #print(ret)
    return ret

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port id", type=int, default=5006)
    parser.add_argument("-l", "--localhost", help="local host", type=int, default=1)
    args = parser.parse_args()

    if args.localhost:
        app.run(threaded=True, port=args.port, debug=True)
    else:
        # set port into 5000 and debug is True
        app.run(threaded=True, port=args.port, debug=False, host="0.0.0.0")    # 开启对外服务