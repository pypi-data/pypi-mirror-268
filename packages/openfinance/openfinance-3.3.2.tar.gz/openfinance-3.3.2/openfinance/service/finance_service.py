# -*- coding: utf-8 -*-
# (C) Run, Inc. 2022
# All rights reserved (Author BinZHU)
# Licensed under Simplified BSD License (see LICENSE)

import os
import sys
import time
import datetime
import argparse
import threading

from flask import Flask, request, jsonify

from openfinance.utils.log import get_logger
from openfinance.service.error import StatusCodeEnum
from openfinance.service.auth.login import LoginManager

from openfinance.config import Config
from openfinance.agentflow.llm.manager import ModelManager 
from openfinance.searchhub.channel.analysis.test_analysis import analysis_with_role
from openfinance.searchhub.channel.function.test_function import search
from openfinance.searchhub.channel.role.test_character import role

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

logger = get_logger("finance.log")
login_manager = LoginManager("accounts")

config = Config()
model_manager = ModelManager(config=config)
llm = model_manager.get_model("chatgpt")

@app.route('/', methods = ['GET', 'POST'])
def connect():
    logger.info("recieve request")
    ret = jsonify(message = "Congrats! Connected!", status = StatusCodeEnum.OK.code)
    logger.info('output: {}'.format(ret.data.decode('utf8')))
    return ret

@app.route('/register', methods=['POST'])
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

def call_process(input_data):
    print(input_data)
    query = input_data['query']
    if query.startswith("@analysis"):
        print("1")
        query = query[len("@analysis"):]        
        result = analysis_with_role(query, llm)
    elif query.startswith("@search"):
        print("2")
        query = query[len("@search"):]
        result = search(query, llm)
    elif query.startswith("@buffett"):
        print("3")
        query = query[len("@buffett"):]        
        result = role(query, llm, "buffett")
    else:
        print("4")        
        result = generate(llm, query)
    print("result", result)
    return result, StatusCodeEnum.OK

@app.route('/query', methods=['POST'])
def query():
    #start_time = time.time()
    data = request.get_json(force=True)
    #logger.info('input: {}'.format(data))
    result = ""

    try:
        #err = login(data)    # login success
        #if err.code == 0:
        result, err = call_process(data)
        ret = jsonify(candidate = result,
                                    msg = err.msg, 
                                    ret_code = err.code)
    except:
        #logger.error(f"request_id: {data['header']['req_id']}")
        ret = jsonify(candidate = result,
                                    msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                                    ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    
    #end_time = time.time()
    #logger.info(f"cost time: {end_time - start_time}")
    #logger.info(f'output: {ret.data.decode("utf8")}')
    return ret

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port id", type=int, default=5001)
    parser.add_argument("-l", "--localhost", help="local host", type=int, default=1)
    args = parser.parse_args()

    if args.localhost:
        app.run(threaded=True, port=args.port, debug=True)
    else:
        # set port into 5000 and debug is True
        app.run(threaded=True, port=args.port, debug=False, host="0.0.0.0")    # 开启对外服务