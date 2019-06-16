from django.urls import path, include
from . import views #home page view will be based in products

urlpatterns = [
	path('signup', views.signup, name='signup'), #defined url reference from main urls.py to views.py
	path('login', views.login, name='login'), #defined url reference from main urls.py to views.py
	path('logout', views.logout, name='logout'), #defined url reference from main urls.py to views.py
]