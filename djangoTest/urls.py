"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djtest import views as djtest_view
from djtest.controller import indexController as indexController
from djtest.controller import personController as personController

urlpatterns = [
    path('',indexController.index),
    path('admin/', admin.site.urls),
    path('index.html',indexController.index),
    path('add.html',djtest_view.add,name='add'),
    path('addAjax.html',djtest_view.addAjax,name='addAjax'),
    path('home.html',djtest_view.home,name='home'),
    path('person.html',personController.person),
    path('addPerson.html',personController.addPerson),
]
