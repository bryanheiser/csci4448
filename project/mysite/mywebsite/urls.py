from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home, name='Home'),
	path('login/', views.LogIn, name='LogIn'),
	path('cart/', views.CartPage, name='CartPage'),
	path('signup/', views.SignUp, name='SignUp'),
	path('bat_board/', views.BatBoard, name='BatBoard'),
	path('vol_jacket/', views.VolJacket, name='VolJacket'),
	path('burt_mittens/', views.BurtMittens, name='BurtMittens'),
	path('line_skis/', views.LineSkis, name='LineSkis'),
	path('von_goggles/', views.VonGoggles, name='VonGoggles'),
	path('686_jacket/', views._686Jacket, name='_686Jacket'),
	path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]
