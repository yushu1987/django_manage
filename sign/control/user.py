#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/7/12'

from django.http import HttpResponse
from sign.config import const
from sign.lib.util import generator_exception_response
from sign.service.user_service import UserService
import json

def get_user_info(request):
    uid = request.GET.get('uid', 0 )
    if uid == 0:
        return HttpResponse(generator_exception_response(const.PARAM_INVALID))
    user = UserService(uid)
    return HttpResponse(json.dumps(user.get_user_info()))

