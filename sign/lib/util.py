#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import functools
from sign.config import const

__mtime__ = '2017/7/12'
from sign.config.error_code import error_code
def generator_exception_response(error):
    try:
        error_msg = error_code[error]
        response = {'error': int(error), 'msg': error_msg, 'data':{}}
        return json.dumps(response)
    except:
        error_msg = error_code['1']
        response={'error':1, 'msg':error_msg,'data':{}}
        return json.dumps(response)

def check_input_int(func):
    @functools.wraps(func)
    def must_int(*args,**kwargs):
        request = args[0]
        uid = request.GET.get('uid', 0)
        if uid == 0:
            return generator_exception_response(const.PARAM_INVALID)
        else:
            return func(*args, **kwargs)
    return must_int


def decorator_try_catch(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return json.loads(generator_exception_response(const.USER_NOT_EXIST))
    return inner

