"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('mywebsite/', include('mywebsite.urls')),
    	path('mywebsite/login/', include('mywebsite.urls')),
	path('mywebsite/cart/', include('mywebsite.urls')),
	path('mywebsite/signup/', include('mywebsite.urls')),
	path('mywebsite/bat_board/', include('mywebsite.urls')),
	path('mywebsite/vol_jacket/', include('mywebsite.urls')),
	path('mywebsite/burt_mittens/', include('mywebsite.urls')),
	path('mywebsite/line_skis/', include('mywebsite.urls')),
	path('mywebsite/von_goggles/', include('mywebsite.urls')),
	path('mywebsite/686_jacket/', include('mywebsite.urls')),
	path('mywebsite/add_to_cart/', include('mywebsite.urls')),
	path('admin/', admin.site.urls)
]
