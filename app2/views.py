from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    from django.urls import reverse
    return HttpResponse(reverse('app2:index'))