from django.urls import path
from .views import *

urlpatterns = [
    path('detail_view/<int:user_id>/', page1_view, name='detail_view'),
    path("accountlogin",login_view,name="accountlogin"),
    path("accountregistration",registration_view,name="accountregistration"),
    path("",alluser,name="alluserdetail"),
    path('register/', register_user, name='register_user'),
    path('addproduct/', addproduct_view, name='add_product'),

]
