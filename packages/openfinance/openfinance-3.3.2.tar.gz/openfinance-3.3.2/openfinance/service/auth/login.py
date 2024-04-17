# -*- coding: utf-8 -*-
# (C) Run, Inc. 2023
# All rights reserved (Author BinZHU)
# Licensed under Simplified BSD License (see LICENSE)

import os
import sys
import time
import json
from hashlib import md5
from flask import jsonify

from openfinance.service.error import StatusCodeEnum
from openfinance.utils.log import get_logger


class LoginManager:
  def __init__(self, name="account"):
    self.accounts = {}
    self.account_path = os.path.join(
      os.path.dirname(__file__), name + ".json")
    if os.path.exists(self.account_path):
      with open(self.account_path, "r") as infile:
        accounts = json.load(infile)
        for d in accounts:
          self.accounts[d["user"]] = d["passwd"]
    #print (self.accounts)

  def register(self, user, passwd):
    if user is None or passwd is None:
      return StatusCodeEnum.NECESSARY_PARAM_ERR
    if user in self.accounts and self.accounts[user] == passwd:
      return StatusCodeEnum.USER_EXIST
    self.accounts[user] = passwd
    account_json = []
    for u, p in self.accounts.items():
      account_json.append(
        {
          "user": u,
          "passwd": p
        }
      )
    with open(self.account_path, "w") as outfile:
      json.dump(account_json, outfile, ensure_ascii=False, indent=4)
    return StatusCodeEnum.OK

  def login(self, user, passwd):
    if user is None or passwd is None:
      return StatusCodeEnum.NECESSARY_PARAM_ERR    
    if user not in self.accounts:
      return StatusCodeEnum.USER_ERR
    if passwd != self.accounts[user]:
      return StatusCodeEnum.PWD_ERR
    return StatusCodeEnum.OK

  def login_with_token(self, user, prefix, token):
    r'''
      校验token: 
      a = str(前缀prefix) + passwd
      b = md5(a) # 16进制
    '''
    if user is None or token is None:
      return StatusCodeEnum.NECESSARY_PARAM_ERR    
    if user not in self.accounts:
      return StatusCodeEnum.USER_ERR
    check_token = md5((str(prefix) + self.accounts[user]).encode('utf8'))
    if token != check_token.hexdigest():
      return StatusCodeEnum.PWD_ERR
    return StatusCodeEnum.OK


if __name__ == '__main__':
  manager = LoginManager("test")
  print(manager.register("2", "2"))
  print(manager.register("2", "2"))
  print(manager.register("2", "3"))
  print(manager.login("2", "2"))
  print(manager.login("2", "3"))
  print(manager.login("3", "2"))  