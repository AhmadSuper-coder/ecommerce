from django.urls import path
from . import views


urlpatterns = [
  path("",views.Home_view,name="home"),
  path("shop",views.Shop_view,name="shop"),
  path('detail/', views.detail_view, name='detail'),
  path('cart/', views.cart_view, name='cart'),
  path('checkout/', views.checkout_view, name='checkout'),
  path('contact/', views.contact_view, name='contact'),
]

