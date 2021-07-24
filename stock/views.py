from django.shortcuts import render
from . import stock

def home(self):
    stock.information_delete()
    stock.information_save(['215000','121440','070960','035250','007720','122450','308100','019010','025980','110790','294870'])
    return render(self, 'stock/home.html')