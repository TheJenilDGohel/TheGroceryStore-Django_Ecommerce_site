from django.contrib import admin
from django.urls import path

from . import views
from .views import Home,Cart,category,checkout,shop,Wishlist,Orders,Search,user_profile

urlpatterns = [
    path('',Home.as_view() , name= 'home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('shop',shop.as_view(),name='shop'),
    path('cart/',Cart.as_view(),name="cart"),
    path('category/',views.category,name="category"),
    path('clear_cart/',views.clear_cart,name="clear_cart"),
    path('review',views.review,name='review'),
    path('checkout/',views.checkout,name='checkout'),
    path('wish_list/',Wishlist.as_view(),name='wishlist'),
    path('orders/',Orders.as_view(),name='orders'),
    path('search_products/',Search.as_view(),name='search'),
    path('user_profile/',views.user_profile,name='userprofile'),
]
