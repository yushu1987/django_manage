#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

__mtime__ = '2017/8/2'

class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField("event_time")
    create_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
