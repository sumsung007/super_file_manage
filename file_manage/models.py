# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from file_manage.permission_list import permission_list

# Create your models here.

class UserInfo(User):
    class Meta:
        permissions = permission_list
        