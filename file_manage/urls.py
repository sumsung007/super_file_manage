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
    url('^index$',                          views.index,        name='index'),
    url('^login$',                          views.user_login,   name='login'),
    url('^logout$',                         views.user_logout,  name='logout'),
    url('^user_manage',                     views.user_manage,  name='user_manage'),
    url('^no_permission',                   views.no_permission,name='no_permission'),
]

urlpatterns += [
    url('^api/request_file_tree$',          views_api.request_file_tree,name='request_file_tree'),
    url('^api/create_dir$',                 views_api.create_dir,       name='create_dir'),
    url('^api/rename_dir$',                 views_api.rename_dir,       name='rename_dir'),
    url('^api/delete_dir$',                 views_api.delete_dir,       name='delete_dir'),
    url('^api/request_file_list$',          views_api.request_file_list,name='request_file_list'),
    url('^api/add_files$',                  views_api.add_files,        name='add_files'),
    url('^api/request_page_mode$',          views_api.request_page_mode),
    url('^api/mv_dir$',                     views_api.mv_dir,           name='mv_dir'),
    url('^api/request_user_list$',          views_api.request_user_list,name='request_user_list'),
    url('^api/create_user$',                views_api.create_user,      name='create_user'),
    url('^api/update_user$',                views_api.update_user,      name='update_user'),
    url('^api/delete_user$',                views_api.delete_user,      name='delete_user'),
    url('^api/change_password$',             views_api.change_password, name='change_password'),
    url('^api/request_permission_list$',    views_api.request_permission_list),
]
