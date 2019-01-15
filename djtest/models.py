#coding:utf-8
from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.id + "," + self.username + "," + self.password + "," + self.age



