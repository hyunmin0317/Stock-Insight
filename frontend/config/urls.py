from django.contrib import admin
from django.urls import path
from stock import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
]
