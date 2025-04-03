from django.urls import path
from .views import *

urlpatterns = [
    path("accounthome/",page1_view,name="accounthomepage"),
    path("accountlogin",login_view,name="accountlogin"),
    path("accountregistration",registration_view,name="accountregistration"),

]
