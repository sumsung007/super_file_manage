# -*- coding: utf-8 -*-
import datetime, urllib, time, random

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from django.db.models import F
from django.db.models import Count, Max

from common.exceptions import UBoxException
from common import Utils




