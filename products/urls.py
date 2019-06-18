from django.urls import path, include
from . import views #home page view will be based in products

urlpatterns = [
	path('create', views.create, name='create'), #defined url reference from main urls.py to views.py
	path('<int:product_id>', views.detail, name='detail'), #product detail path
	path('<int:product_id>/upvote', views.upvote, name='upvote'),
]