from django.shortcuts import render,HttpResponse
from django.urls import reverse
# Create your views here.

#必须传入requets参数，request参数是是请求的参数，使用时直接request.就可以取出当中的请求参数
def timer(request):
    import time
    ctime = time.time()

# 后续不管是从服务器中取出的数据还是任何数据，都是以最后一个参数字典形式传入到html文件中
    return render(request,"timer.html",{"ctime":ctime})

def login(request):

    if request.method == "GET":
        return render(request,"login.html")
    else:
        # 使用request获取form表单提交的数据
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'wualin' and pwd == '123':
            return HttpResponse('登陆成功')
        else:
            return HttpResponse("用户名或者密码错误")

def year_archive(request,year):
    #使用django.urls模块下的reverse模块进行反向解析

    # url = reverse('y_a',args=(3000,))
    # print(url) #/app1/articles/2000/
    # HttpResponse返回的参数时一哥字符串
    return HttpResponse("<h1>%s</h1>"%(year))

def month_archive(request,year,month):


    return HttpResponse("<h1>年：%s 月：%s</h1>"%(year,month))


def index(request):
    #请求路径
    print(request.path)
    #请求路径以及请求参数
    print(request.get_full_path())
    #get请求的参数
    print(request.GET)
    #post请求的参数
    print(request.POST)

    # return HttpResponse(reverse('app1:index'))
    # import time
    # now = time.time()
    # return render(request,'index.html',{'time':now})
    # ---------{{ }}
    name = 'name'
    lis = [1,2,3,4,5,6]
    dic = {"name":"wualin","age":21}
    class Person(object):
        def __init__(self,name,age):
            self.name = name
            self.age = age
    alex = Person("alex",19)
    egon = Person("egon",22)
    person_list = [alex,egon]
    import datetime
    now = datetime.datetime.now()
    lis = []
    user = "alex"
    i = 10
    filesize = 145234563
    text = "文本内容文本内容文本内容文本内容文本内容文本内容文本内容文本内容文本内容"

    # ---------标签{% %}




    return render(request,'index.html',locals())
