#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/7/12'
from sign.models import User
import time
from sign.lib.util import decorator_try_catch

class UserService(object):
    def __init__(self, uid):
        self.uid = uid

    @decorator_try_catch
    def get_user_info(self):
        user_info = User.objects.get(id=self.uid)
        user_info = {
            'username':user_info.username,
            'password':user_info.password,
            'create_time':time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(user_info.create_time))
        }
        return user_info
