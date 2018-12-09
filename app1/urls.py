from django.contrib import admin
from django.urls import path,re_path,include
from app1 import views

urlpatterns = [
    re_path(r'^index',views.index,name='index'),
    # re_path(r'^articles/([0-9]{4})/$',views.year_archive,name='y_a'),# 匹配成功之后会将匹配成功的内容传入到year_archive函数中，在views定义函数时要接收两个参数
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.month_archive,name='m_a'),
    path("articles/<int:year>/",views.year_archive,name='y_a'),
    path("timer/",views.timer),
    path("dborm/",views.dborm),
    path("book/",views.book),
    path("add_book/",views.add_book),
        path("book/<int:num>/edit",views.edit),
    path("book/<int:num>/delete",views.del_date)
]