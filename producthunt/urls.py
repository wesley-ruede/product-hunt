
from django.contrib import admin
from django.urls import path, include
from products import views #home page view will be based in products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #product views path, empty string as reference to home, and views.home is a function of product views
    path('accounts/', include('accounts.urls')),
]