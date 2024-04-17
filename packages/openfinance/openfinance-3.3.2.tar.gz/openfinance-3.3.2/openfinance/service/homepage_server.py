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
from openfinance.datacenter.knowledge.executor import ExecutorManager
from openfinance.searchhub.page_manage.factor import FactorManager
from openfinance.searchhub.page_manage.model import ModelManager

from openfinance.datacenter.knowledge.graph import Graph
from openfinance.searchhub.recall.channel import analysis
from openfinance.service.base import wrapper_return

from openfinance.config import Config

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
CORS(app, resources=r'/*')

logger = get_logger("homepage.log")
login_manager = LoginManager("accounts")

config = Config()

graph = Graph.build_from_file(
    "openfinance/datacenter/knowledge/schema.md"
)
graph.assemble(ExecutorManager())
model_manager = ModelManager(graph)
factor_manager = FactorManager(graph)

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


@app.route('/api/category', methods=['GET'])
def category():
    #print("enter")    
    #data = request.get_json(force=True)
    #print(data)
    try:
        data = factor_manager.get_homepage(20)
        ret = jsonify (category = data,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)
    except:
        ret = jsonify (category = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

@app.route('/api/models', methods=['POST'])
def models():
    data = request.get_json(force=True)
    print(data)    
    try:
        factor = ""
        if 'factor' in data['data']:
            factor = data['data']['factor']
        if factor:
            data = model_manager.get_factor_model(factor, 20)
        else:
            data = model_manager.get_homepage(20)

        ret = jsonify (models = data,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)
    except:
        ret = jsonify (models = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret


@app.route('/api/updateCode', methods=['POST'])
def updateCode():
    data = request.get_json(force=True)
    print(data)    
    try:
        factor = data['data'].get('factor', "")
        model = data["data"].get("model", "")
        code = data["data"].get("code", "")
        text = data["data"].get("text", "")
        #user = "default"
        #eval(code)
        ret = jsonify (models = data,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)
    except:
        ret = jsonify (models = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

@app.route('/api/eval', methods=['POST'])
def eval():
    data = request.get_json(force=True)
    print(data)    
    try:
        factor = data['data'].get('factor', "")
        model = data["data"].get("model", "")
        text = data["data"].get("input", "")
        
        if text:
            result = ExecutorManager().get(factor).func(text)
        else:
            result = ExecutorManager().get(factor).func()

        data = wrapper_return(result)
        ret = jsonify (data = data,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)
    except Exception as e:
        print(e)
        ret = jsonify (data = {"result": e},
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    #print(ret)
    return ret

#  A new version for model user parameter is required
@app.route('/api/getCode', methods=['POST'])
def getCode():
    data = request.get_json(force=True)
    print(data)
    try:
        factor = data['data'].get('factor', "")
        user = data["data"].get("author", "")
        #user = "default"
        code = inspect.getsource(
            ExecutorManager().get(factor).func
        )
        text = ExecutorManager().get(factor).description
        data = {
            "version": "v1.0.0",
            "code": code,
            "text": text
        }
        ret = jsonify (models = data,
                        msg = StatusCodeEnum.OK.msg, 
                        ret_code = StatusCodeEnum.OK.code)
    except:
        ret = jsonify (models = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    print(ret)
    return ret

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port id", type=int, default=5003)
    parser.add_argument("-l", "--localhost", help="local host", type=int, default=1)
    args = parser.parse_args()

    if args.localhost:
        app.run(threaded=True, port=args.port, debug=True)
    else:
        # set port into 5000 and debug is True
        app.run(threaded=True, port=args.port, debug=False, host="0.0.0.0")    # 开启对外服务