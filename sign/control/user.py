#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/7/12'

from django.http import HttpResponse
from sign.config import const
from sign.lib.util import (generator_exception_response,check_input_int)
from sign.service.user_service import UserService
import json

@check_input_int
def get_user_info(request):
    uid = request.GET.get('uid', 0 )
    user = UserService(uid)
    user_info = user.get_user_info()
    print user_info
    return HttpResponse(json.dumps(user_info))

