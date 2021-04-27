from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request,'home.html') #使用视图函数 返还一个httpresponse  这是测试内容通关的关键