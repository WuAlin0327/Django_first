from django.shortcuts import render,HttpResponse,redirect
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

from app1.models import Book #添加models中定义好的ORM类
def dborm(request):
    #添加表记录
    #方式1
    # book_obj = Book(id=1,title='python',price=99.9,pub_date='2018-12-9',publish='人民币出版社')
    # book_obj.save()
    #方式2 create是有返回值的，返回值是当前生成的记录，使用.可以进行调用
    # book_obj = Book.objects.create(title='射雕英雄传',price=2000.9,pub_date='2018-12-8',publish='清华出版社')

    #查询
    # all()
    # book_list = Book.objects.all()  #查询所有，返回值是QuerySet，支持for循环以及切片操作
    # #book_list是一个Django自己的数据类型：QuerySet，可以使用列表的方法去处理他
    # for obj in book_list:
    #     print(obj.title)
    # first()
    # book = Book.objects.first()
    # print(book)
    # filter()
    # book = Book.objects.filter(id=1)
    # print(book[0].title)

    # book = Book.objects.get(id=1)
    # print(book.title)

    # book = Book.objects.exclude(title='python')
    # print(book[1].title)
    # 默认升序
    # book = Book.objects.all().order_by('id')
    # print(book)
    # book = Book.objects.all().count()
    # print(book)
    # book = Book.objects.all().exists()
    # print(book)# True
    # book = Book.objects.all().values('id','price')
    # #<QuerySet [{'id': 1, 'price': Decimal('99.90')}, {'id': 2, 'price': Decimal('22.90')}, {'id': 3, 'price': Decimal('2000.90')}]>
    # print(book)

    # book = Book.objects.all().values_list('title')
    # print(book)
    # book = Book.objects.all().values('price').distinct()
    # print(book)
    # book = Book.objects.filter(pub_date__year=2018,title='python')
    book = Book.objects.filter(title='python').update(title='Django WEB开发')
    print(book)
    return HttpResponse('ok')

def book(request):
    if request.method == 'GET':
        book_date = Book.objects.all()
        print(book_date)
        return render(request,'book.html',{'book_data':book_date})
    else:
        id = request.POST.get('id')
        if id == None:
            Book.objects.create(title=request.POST.get('book_name'),price=request.POST.get('price'),pub_date=request.POST.get('pub_date'),publish=request.POST.get('publish'))
            book_date = Book.objects.all()
            return render(request, 'book.html', {'book_data': book_date})
        else:
            book_name = request.POST.get('book_name')
            price = request.POST.get('price')
            pub_date = request.POST.get('pub_date')
            publish = request.POST.get('publish')
            Book.objects.filter(id=id).update(title=book_name,price=price,pub_date=pub_date,publish=publish)
            book_date= Book.objects.all()
            return render(request,'book.html',{'book_data':book_date})

def edit(request,num):
    book_date = Book.objects.get(id=num)
    return render(request, 'edit.html', {"book_date": book_date})

def del_date(request,num):
    Book.objects.filter(id=num).delete()
    #让delete.html帮忙刷新一下

    # redirect重定向
    return redirect('/app1/book/')

def add_book(request):
    return render(request,'add_book.html')