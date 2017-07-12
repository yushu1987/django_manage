#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import functools

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


def decorator_try_catch(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except :
            return json.loads(generator_exception_response('1'))
    return inner

