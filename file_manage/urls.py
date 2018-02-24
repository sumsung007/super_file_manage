# -*- coding: utf-8 -*-

"""GlobalSettings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views, views_api

urlpatterns = [
    url('^index$',                         views.index),
    url('^login$',                         views.user_login, name='login'),
    url('^logout$',                         views.user_logout, name='logout'),
]

urlpatterns += [
    url('^api/request_file_tree$',          views_api.request_file_tree),
    url('^api/create_dir$',                 views_api.create_dir),
    url('^api/rename_dir$',                 views_api.rename_dir),
    url('^api/delete_dir$',                 views_api.delete_dir),
    url('^api/request_file_list$',          views_api.request_file_list),
    url('^api/add_files$',                  views_api.add_files),
    url('^api/request_page_mode',           views_api.request_page_mode),
    url('^api/mv_dir',                      views_api.mv_dir),
]
