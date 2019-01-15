#conding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return render(request,'home.html')

#add.html?a=4&b=5
def add(request):
    return render(request, 'add.html')


def addAjax(request):
    a = request.POST.get('a', 0)
    b = request.POST.get('b', 0)
    c = int(a) + int(b)
    res = {'code':0,'res':c}
    return JsonResponse(res)