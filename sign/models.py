from __future__ import unicode_literals

from django.db import models
import time
import json

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    create_time = models.IntegerField()


