from django import template

# 该对象名必须是register
register = template.Library()

#自定义过滤器装饰器
@register.filter
def multi_filter(x,y):
    return x*y

#自定义标签装饰器
@register.simple_tag
def multi_tag(x,y):
    return x*y