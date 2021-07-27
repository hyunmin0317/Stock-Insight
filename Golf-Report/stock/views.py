from django.shortcuts import render
from .models import Information, Date
from . import stock

code_list = ['215000', '121440', '070960', '035250', '007720', '122450', '308100', '019010', '025980', '110790', '294870', '288490', '183410', '206950', '300120', '005720', '017960', '034300', '081660']

def home(request):
    name = []
    name_list = []
    information_list = Information.objects.all()
    data_list = Date.objects.all()

    for i in information_list:
        name.append(i.stock.name)

    for n in name:
        if n not in name_list:
            name_list.append(n)

    context = {'name_list': name_list, 'data_list': data_list}
    return render(request, 'stock/home.html', context)

def save_code(request):
    stock.stock_delete()
    stock.stock_save()
    return render(request, 'save.html')

def save_data(request):
    stock.information_delete()
    stock.information_save(code_list)
    stock.date_delete()
    stock.date_save()
    return render(request, 'save.html')