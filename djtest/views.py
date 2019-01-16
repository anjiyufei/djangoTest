#conding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect

def home(request):
    return render(request,'home.html')


def sum(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def sum2(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    c = int(a) + int(b)
    context = {'c':c}
    #context['c'] = str(c)
    return render(request,'sum.html',context)

def login2(request):
    return redirect('login.html?err=2')

def login(request):
    err = request.GET.get('err', 0)
    context = {'err':err}
    #context['err'] = str(err)
    return render(request, 'login.html', context)

def add(request):
    return render(request, 'add.html')


def addAjax(request):
    a = request.POST.get('a', 0)
    b = request.POST.get('b', 0)
    c = int(a) + int(b)
    res = {'code':0,'res':c}
    return JsonResponse(res)