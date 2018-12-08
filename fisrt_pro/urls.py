"""fisrt_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 给这一个url命名为log，然后在login.html中form表单往什么url提交时以{% url 'log' %}
    path('login.html/', views.login,name='log'),

    #year_archive(request,year)
    # re_path(r'^articles/([0-9]{4})/$',views.year_archive),# 匹配成功之后会将匹配成功的内容传入到year_archive函数中，在views定义函数时要接收两个参数
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.month_archive)

    re_path(r'^app1/', include(("app1.urls","app1"))),
    re_path(r'^app2/', include(("app2.urls","app2")))
]
