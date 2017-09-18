#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/7/12'

from django.http import JsonResponse
from sign.lib.util import (check_input_int)
from sign.service.user_service import UserService

@check_input_int
def get_user_info(request):
    uid = request.GET.get('uid', 0)
    user = UserService(uid)
    user_info = user.get_user_info()
    print user_info
    return JsonResponse(user_info)

