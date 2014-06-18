from django.db import models
from random import randrange
from datetime import datetime, timedelta
from hashlib import md5

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user = models.Foreignkey(User)
    user_image = models.TextField(null=True, blank=True)
    activation_key = models.IntegerField(null=True, blank=True)
    key_expires = models.DateTimeField(null=True, blank=True)
    dept = models.TextField(null=True, blank=True)


class ClientProfile(models.Model):
    client = models.ForeignKey(User)
    dept = models.TextField(null=True,blank=True)
    question = models.TextField(max_length=None)

class ClientChat(models.Model):
    client = models.ForeignKey(ClientProfile)
    asst = models.ForeignKey(UserProfile)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True,blank=True)
    content = models.TextField(max_length=None)

    def duration(self):
        duratn = (ended_at-started_at)

class OperatorChat(models.Model):
    frm_op = models.ForeignKey(UserProfile)
    to_op = models.ForeignKey(UserProfile)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True,blank=True)
    content = models.TextField(max_length=None)

    def duration(self):
        duratn = (ended_at-started_at)

