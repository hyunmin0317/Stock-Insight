from django.contrib import admin
from django.urls import path, include
from stock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save/code/', views.save_code),
    path('save/data/', views.save_data),
    path('front/', views.front),
    path('stock/', include('stock.urls')),
]
