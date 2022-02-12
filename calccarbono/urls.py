from django.contrib import admin
from django.urls import path, include
from .views import teste_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste_django),
    path('', include('carbonoapp.urls')),
    path('', include('carbonoapp.urls')),
]
