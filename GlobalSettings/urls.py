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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^test.html$', TemplateView.as_view(template_name='link.html', content_type='text/html')),
    url(r'^admin/', admin.site.urls),


    url(r'^file_manage/',            include('file_manage.urls')),             # 入口
]

# 为了在使用runserver命令起服务时能正常获取media/下的内容
# 在linux上线时可以关闭，因为在正式部署时，media目录是通过apache控制的
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

