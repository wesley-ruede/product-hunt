
from django.contrib import admin
from django.urls import path, include
from products import views #home page view will be based in products
from django.conf import settings
from django.conf.urls.static import static #imports static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #product views path, empty string as reference to home, and views.home is a function of product views
    path('accounts/', include('accounts.urls')), #forward to account -- urls.py
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #image views