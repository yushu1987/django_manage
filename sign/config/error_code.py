#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/7/12'
import const

const.PARAM_INVALID = '100'
const.COMMON_ERROR = '1'
const.USER_NOT_EXIST = '10'

error_code = {
    const.COMMON_ERROR: '访问异常',
    const.PARAM_INVALID : '参数错误',
    const.USER_NOT_EXIST : '用户不存在'
}
