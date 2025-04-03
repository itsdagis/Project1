from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("usersitehome/",page3_view,name="usersitehomepage"),
    path("usersitehomepage/",userhome_view,name="usersitehome"),
    path("usersiteorder/",userorder_view,name="usersiteorderpage"),
]
