# -*- coding: utf-8 -*-
import datetime, random

from django.db import models
from main.choices import CLASS_CHOICES,CLASS_MAPS
from common.Define import LINK_FLAG_CHOICES, VIDEO_PLAY_AUTH_CHOICES, VERSION_CHOICES
from .choices import RECOMMEND_TYPE_CHOICES, RECOMMEND_TYPE
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)
from file_manage.permission_list import permission_list1






