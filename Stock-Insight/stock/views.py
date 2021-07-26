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

def show(request):
    date_list = []
    information_list = Information.objects.all()
    for i in information_list:
        date_list.append(i.date)
    date_list = set(date_list)

    data_list = Date.objects.all()

    # data = []
    # data.append([1,2,3])
    # data.append([4,5,6])

    '''
    [2020.03, 골프존, 골프존뉴딘홀딩스, 100, 500, 200]
    [2020.06, 골프존, 200, 100, 500, 200]
    ...
    '''

    context = {'information_list': information_list, 'data_list':data_list}
    return render(request, 'stock/show.html', context)