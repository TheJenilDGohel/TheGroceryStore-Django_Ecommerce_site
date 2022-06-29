from django.contrib import admin
from django.urls import path,include
from .views import Login

from . import views 

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',Login.as_view(),name="login"),
    path('logout/',views.logout,name="logout"),
    ]
