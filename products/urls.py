from django.urls import path, include
from . import views #home page view will be based in products

urlpatterns = [
	path('create', views.create, name='create'), #defined url reference from main urls.py to views.py
]