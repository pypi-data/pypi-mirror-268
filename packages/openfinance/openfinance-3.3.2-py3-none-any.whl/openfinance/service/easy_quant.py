# -*- coding: utf-8 -*-
# (C) Run, Inc. 2022
# All rights reserved (Author BinZHU)
# Licensed under Simplified BSD License (see LICENSE)

import os
import sys
import time
import datetime
import argparse
from flask import Flask, request, jsonify

from openfinance.strategy.operator.base import OperatorManager
from openfinance.service.error import StatusCodeEnum

from openfinance.strategy.policy.company_ranker import CompanyIndexSort

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

company_ranker = CompanyIndexSort.from_file()

@app.route('/', methods=['GET', 'POST'])
def connect():

    ret = jsonify(message="Congrats! Connected!",
                  status=StatusCodeEnum.OK.code)
    return ret

def get_predict(inputs):
    return OperatorManager().get(
        inputs['factor']
    ).run(data=inputs['quant_data'], latest=False)

@app.route('/quant/calc', methods=['POST'])
def predict():
    start_time = time.time()
    data = request.get_json(force=True)
    result = get_predict(data)
    print(result)
    end_time = time.time()
    ret = jsonify(result=result,
                  message=StatusCodeEnum.OK.msg,
                  status=StatusCodeEnum.OK.code)
    return ret

@app.route('/api/quant/factor', methods=['GET'])
def factor():
    try:
        factors = list(company_ranker.name_to_features.keys())
        mode = ["gt", "lt", "in"]
        ret = jsonify ( result = {"factor": factors, "mode": mode},
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)        
    except Exception as e:
        print(e)
        ret = jsonify ( result = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

@app.route('/api/quant/fetch', methods=['POST'])
def fetch():
    try:
        data = request.get_json(force=True)
        params = []
        for i in data["data"]:
            params.append(
                (i["factor"], i["mode"], i["val"])
            )
        candidates = company_ranker.fetch(
            params=[
                # ("OperationGrow", "gt", 10), 
                # ("DividentMean", "gt", 3),
                # ("DividentSpeed", "gt", 0.1),            
                # ("OperationSpeedAcc", "lt", 10),
                # ("ProfitGrow", "gt", 10),
                # ("ProfitSpeedAcc", "lt", 10),
                # ("GrossProfit", "gt", 100),
                ("PriceEarning", "lt", 80),
                ("PriceEarning", "gt", 10) 
                # ("MoneyFlowDirect", "gt", 0)
            ]
        )
        features = policy.features(
            candidates=candidates,
            from_db=True,
            type="company"
        )
        ret = jsonify ( result = features,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)        
    except Exception as e:
        print(e)
        ret = jsonify ( result = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port id", type=int, default=5001)
    parser.add_argument("-l", "--localhost",
                        help="local host", type=int, default=1)
    args = parser.parse_args()

    if args.localhost:
        app.run(port=args.port, debug=True)
    else:
        # set port into 5000 and debug is True
        app.run(port=args.port, debug=False, host="0.0.0.0")  # 开启对外服务

