import json

from django.core import serializers
from django.http import HttpResponse
from djtest import models
from django.shortcuts import render
from django.http import JsonResponse

from djtest.models import Person


def person(request):
    return render(request,'person.html')

def addPerson(request):
    if request.method == "POST":
        if request.POST.get("username"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            age = request.POST.get("age", 1)
            models.Person.objects.create(username=username,password=password,age=age)
        else:
            res = {"code": 1}
    #
    user_list = Person.objects.all().values('id','username','password','age')
    # data = serializers.serialize('json', user_list)

    #user_list = models.Person.objects.filter(age>10).values('id','username','age')
    #user_list = Person.objects.filter(age__gt=10).values('id','username','password','age')
    data = json.dumps(list(user_list))
    res = {"code":0,"data":data}
    return JsonResponse(res,safe=False)