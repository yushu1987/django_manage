#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sign.model import event
__mtime__ = '2017/8/2'

class Guest(models.Model):
    event = models.ForeignKey(event.Event)
    realname = models.CharField(max_length=64)
    phone= models.CharField(max_length=11)
    email = models.EmailField()
    sign= models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.realname

class Meta:
    unique_together = ('event', 'phone')
