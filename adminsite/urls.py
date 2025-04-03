from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("adminsitehome/",page2_view,name="adminsitehomepage"),
    path("adminsitehomepage/",home_view,name="adminsitehome"),
    path("adminsiteaddproduct/",addproduct_view,name="adminsiteaddproduct"),
]
