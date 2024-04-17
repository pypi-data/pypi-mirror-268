#! -*- coding: utf-8 -*-
"""
Info: Websocket chatbot
"""
import os
import sys
import time
import json
import datetime
import argparse
import asyncio
import websockets

from openfinance.service.auth.login import LoginManager
from openfinance.searchhub.task.task_manager import TaskManager
from openfinance.agents.role.manager import RoleManager
from openfinance.searchhub.page_manage.user import UserManager
from openfinance.agentflow.llm.manager import ModelManager 
from openfinance.searchhub.query_understand.base import QueryUnderstand

from openfinance.config import Config
from openfinance.utils.log import get_logger
from openfinance.service.error import StatusCodeEnum
from openfinance.service.base import wrapper_return

config = Config()
model_manager = ModelManager(config=config)
user_manager = UserManager(config=config)
task_manager = TaskManager(config=config)
role_manager = RoleManager(config=config)

logger = get_logger("chat.log")
llm = model_manager.get_model("aliyungpt")

headers = {
    'Access-Control-Allow-Origin': 'http://localhost:8000',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization'
}

websocket_users = set()

async def check_user_permit(websocket):
    logger.info(f"new websocket_users:{websocket}")
    websocket_users.add(websocket)
    logger.info(f"websocket_users list:{websocket_users}")
    response_text = """你好～欢迎使用OpenFinance Chat，请参考：
    1、您可以从左侧task列表选择您想调用的任务，如未选择，你可以使用@Task名称 指定对应Task
    2、您可以从左侧company列表选取或者直接搜索您感兴趣的公司，如未选择，请确保问题中包含正确上市公司名称
    3、您可以从左侧role列表选择为您解答问题的角色
    4、目前使用英文输出结果。
    祝您使用愉快.
    """
    response_text = wrapper_return(response_text, StatusCodeEnum.OK)   
    await websocket.send(response_text)

async def call_process(input_data, websocket):
    #print(input_data)
    try:
        json_data = json.loads(input_data)
        logger.info(json_data)
        header = json_data["header"]
        json_data = json_data["data"]
        query = json_data.get("input", "")
        session_id = json_data['session_id']
        chart = {}
        if query: # if not contains query, means return history
            task_info = task_manager.extract_task(query)
            task_name = task_info.get("task", json_data.get("task", ""))  ##
            query = task_info.get("query", "")

            role_info = role_manager.extract_role(query)
            role_name = role_info.get("role", json_data.get("role", ""))
            query = role_info.get("query", "")
            
            # if company passed, use it , else parse from query
            company = json_data.get("company", QueryUnderstand.parse(query).get("company", ""))
            if not task_name and role_name:
                task_name = "role"
            task = task_manager.get_task_by_name(task_name)
            #print("json_data", json_data)
            logger.info(json_data)
            if task:
                result = await task.aexecute(
                    query,
                    company = company,
                    role = json_data.get("role", ""),
                    websocket = websocket
                )
            else:
                # logger.info(f"session_id:{session_id}")
                history = user_manager.get_llm_history(session_id)
                # logger.info(f"history:{history}")
                if history:
                    rsp = await llm.acall(history + query + "\nAssistant:")
                else:
                    # insert snapshot for session
                    user_manager.insert_snapshot(header["user"], session_id, query) 
                    rsp = await llm.acall(query)
                result = {"result" : rsp.content}
            #print("return", json_data, result)
            logger.info(f"result:{result}")
            json_data["output"] = result["result"]
            # cache as result for memory
            if "cache" in result:
                json_data["output"] = result["cache"]
            # insert chat message
            user_manager.insert_history(session_id, json.dumps(json_data))
            #print(result)
        else:
            result = user_manager.get_history(session_id)
        #print(result)
        return wrapper_return(result)
    except Exception as e:
        logger.error(e)
        return wrapper_return("Sorry, GPT need to rest...", StatusCodeEnum.UNKNOWN_ERROR)   

async def recv_user_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        print("recv_text:", websocket.pong, recv_text)
        response_text = await call_process(recv_text, websocket)
        print("response_text:", response_text)
        await websocket.send(response_text)

async def run(websocket, path):
    while True:
        try:
            await check_user_permit(websocket)
            await recv_user_msg(websocket)
        except websockets.ConnectionClosed:
            print("ConnectionClosed...", path)  # 链接断开
            print("websocket_users old:", websocket_users)
            websocket_users.remove(websocket)
            print("websocket_users new:", websocket_users)
            break
        except websockets.InvalidState:
            print("InvalidState...")  # 无效状态
            break
        except Exception as e:
            print("Exception:", e)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port id", type=int, default=5004)
    parser.add_argument("-l", "--localhost",
                        help="local host", type=int, default=1)
    args = parser.parse_args()

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(run, '192.168.0.204', args.port, extra_headers=headers)
        )
    asyncio.get_event_loop().run_forever()