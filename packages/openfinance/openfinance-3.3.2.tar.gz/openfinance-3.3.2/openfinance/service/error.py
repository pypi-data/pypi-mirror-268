# -*- coding: utf-8 -*-
# (C) Run, Inc. 2022
# All rights reserved (Author BinZHU)
# Licensed under Simplified BSD License (see LICENSE)
# @Desc: { 项目枚举类模块 }

from enum import Enum

class StatusCodeEnum(Enum):
    """状态码枚举类"""

    OK = (0, '成功')
    UNKNOWN_ERROR = (-1, '未知错误')
    SERVER_ERR = (500, '服务器异常')

    INPUT_CODE_ERR = (4001, '输入格式错误')
    THROTTLING_ERR = (4002, '访问过于频繁')
    NECESSARY_PARAM_ERR = (4003, '缺少必传参数')
    USER_ERR = (4004, '用户名错误')
    PWD_ERR = (4005, '密码错误')
    USER_EXIST = (4006, '用户名已存在')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def msg(self):
        """获取状态码信息"""
        return self.value[1]