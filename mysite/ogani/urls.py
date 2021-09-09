from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/blog_details/', views.blog_details, name='blog_details'),
    path('shop/', views.shop, name='shop'),
    path('shop_cart/', views.shop_cart, name='shop_cart'),
    path('shop/<int:product_id>/shop_details', views.shop_details, name='shop_details'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
]
