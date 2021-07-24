from django.shortcuts import render
from . import stock

def home(self):
    stock.data_save('삼성전자')
    return render(self, 'stock/home.html')