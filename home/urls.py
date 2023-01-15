from django.urls import path
from .import views

urlpatterns=[
    path('', views.homeview, name='home'),
    path('shop/', views.shop, name='shop'),
    path('singleproduct/', views.homeview, name='single-product'),
    path('contact/', views.homeview, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('myaccount/', views.myaccount, name='myaccount'),
]
