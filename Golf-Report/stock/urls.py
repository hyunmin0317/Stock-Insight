from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [
    path('', views.home, name="home"),
    path('1/', views.one, name="one"),
    path('2/', views.one, name="two"),
    path('3/', views.one, name="three"),
]