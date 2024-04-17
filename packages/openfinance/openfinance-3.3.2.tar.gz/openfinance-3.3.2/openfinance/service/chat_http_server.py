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
from flask_cors import CORS
from openfinance.utils.log import get_logger
from openfinance.service.error import StatusCodeEnum
from openfinance.service.auth.login import LoginManager
from openfinance.searchhub.page_manage.company import CompanyManager
from openfinance.searchhub.page_manage.role import RoleManager
from openfinance.searchhub.page_manage.user import UserManager
from openfinance.searchhub.task.task_manager import TaskManager
from openfinance.config import Config

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
CORS(app, resources=r'/*')

logger = get_logger("chat_home.log")
login_manager = LoginManager("accounts")

config = Config()
company_manager = CompanyManager(config)
role_manager = RoleManager()
user_manager = UserManager(config)
task_manager = TaskManager(config)

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


@app.route('/api/sidebar', methods=['POST'])
def category():
    data = request.get_json(force=True)
    #print(data)
    #print(company_manager.get_homepage(20))
    #print(role_manager.get_homepage(20))
    #print(user_manager.get_snapshot(data["header"]["user"]))
    try:
        data = {
            "stock_list": company_manager.get_homepage(20),
            "role_list": role_manager.get_homepage(20),
            "history_list": user_manager.get_snapshot(data["header"]["user"]),
            "task_list": task_manager.get_tasks()
        }
        print(data)
        ret = jsonify (output = data,
                       msg = StatusCodeEnum.OK.msg, 
                       ret_code = StatusCodeEnum.OK.code)
    except:
        ret = jsonify (output = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    return ret


@app.route('/api/role', methods=['POST'])
def role():
    data = request.get_json(force=True)
    #print(data)
    #print(company_manager.get_homepage(20))
    #print(role_manager.get_homepage(20))
    #print(user_manager.get_snapshot(data["header"]["user"]))
    try:
        data = {
            "role_list": role_manager.get_homepage(20),
        }
        print(data)
        ret = jsonify (output = data,
                       msg = StatusCodeEnum.OK.msg, 
                       ret_code = StatusCodeEnum.OK.code)
    except:
        ret = jsonify (output = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    return ret

@app.route('/api/history', methods=['POST'])
def history():
    data = request.get_json(force=True)
    print(data)
    try:
        data = {
            "result": user_manager.get_history(data["data"]["session_id"]),
        }
        print(data)
        ret = jsonify (output = data,
                       msg = StatusCodeEnum.OK.msg, 
                       ret_code = StatusCodeEnum.OK.code)
    except Exception as e:
        print(e)
        ret = jsonify (output = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
    return ret

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json(force=True)
    print(data)
    #print(company_manager.get_homepage(20))
    #print(role_manager.get_homepage(20))
    #print(user_manager.get_snapshot(data["header"]["user"]))
    try:
        text = data['data']['query']
        #print(text)
        data = {
            "result": company_manager.search(text, 20)
        }
        #print(data)
        ret = jsonify (output = data,
                       msg = StatusCodeEnum.OK.msg, 
                       ret_code = StatusCodeEnum.OK.code)
    except Exception as e:
        ret = jsonify (output = "",
                        msg = StatusCodeEnum.UNKNOWN_ERROR.msg, 
                        ret_code = StatusCodeEnum.UNKNOWN_ERROR.code)
        logger.info(f"exception: {e}")   
    return ret

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port id", type=int, default=5005)
    parser.add_argument("-l", "--localhost", help="local host", type=int, default=1)
    args = parser.parse_args()

    if args.localhost:
        app.run(threaded=True, port=args.port, debug=True)
    else:
        # set port into 5000 and debug is True
        app.run(threaded=True, port=args.port, debug=False, host="0.0.0.0")    # 开启对外服务