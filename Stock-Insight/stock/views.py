from django.shortcuts import render
from .models import Stock, Information, Date
from . import stock
from django.http import JsonResponse
from django.core.paginator import Paginator

def home(request):
    page = request.GET.get('page', '1')  # 페이지
    stock_list = []
    code_list = ['215000','121440','070960','035250','007720','122450','308100','019010','025980','110790','294870','288490','183410','206950','300120','005720','017960','034300','081660']

    # stock.stock_delete()
    # stock.stock_save()
    # stock.information_delete()
    # stock.information_save(code_list)
    stock.date_delete()
    stock.date_save()

    for code in code_list:
        try:
            stocks = Stock.objects.get(code=code)
            stock_list.append(stocks)
        except Stock.DoesNotExist:
            return JsonResponse({'message': 'Stock Does Not Exist '}, status=400)

    paginator = Paginator(stock_list, 10)
    page_obj = paginator.get_page(page)
    context = {'stock_list':page_obj}
    return render(request, 'stock/home.html', context)

def detail(request, code):
    try:
        stock = Stock.objects.get(code=code)
    except Stock.DoesNotExist:
        return JsonResponse({'message': 'Stock Does Not Exist '}, status=400)
    information_list = Information.objects.filter(stock=stock)
    context = {'stock':stock, 'information_list': information_list}
    return render(request, 'stock/detail.html', context)

def sales(request):
    name = []
    name_list = []
    information_list = Information.objects.all()
    data_list = Date.objects.all()

    for i in information_list:
        name.append(i.stock.name)

    for n in name:
        if n not in name_list:
            name_list.append(n)

    context = {'name_list': name_list, 'data_list':data_list}
    return render(request, 'stock/sales.html', context)