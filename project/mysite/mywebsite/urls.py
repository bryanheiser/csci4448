from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home, name='Home'),
	path('login/', views.LogIn, name='LogIn'),
	path('cart/', views.Cart, name='Cart'),
	path('signup/', views.SignUp, name='SignUp'),
]
