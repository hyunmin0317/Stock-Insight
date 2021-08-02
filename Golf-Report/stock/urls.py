from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [
    path('', views.home, name="home"),
    path('1/', views.one, name="one"),
    path('2/', views.two, name="two"),
    path('3/', views.three, name="three"),
]