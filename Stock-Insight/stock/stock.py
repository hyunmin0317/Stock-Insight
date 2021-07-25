import pandas as pd
from .models import Stock, Information
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def stock_save():
    data = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
    data = data[['회사명', '종목코드']]
    data = data.rename(columns={'회사명': 'name', '종목코드': 'code'})
    data.code = data.code.map('{:06d}'.format)

    for n in data.name:
        stock = Stock(name=n, code=data.query("name=='{}'".format(n))['code'].to_string(index=False))
        stock.save()

def stock_delete():
    stock = Stock.objects.all()
    stock.delete()

def data_save(code):
    URL = 'https://finance.naver.com/item/main.nhn?code='+code
    data = []
    columns = ['주요재무정보']

    try:
        source_code_from_URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(source_code_from_URL), 'lxml', from_encoding='UTF-8')
        table = soup.find('table', {'class': 'tb_type1 tb_num tb_type1_ifrs'})

        # if(table==None):
        #     return

        thead = table.select_one('thead')
        trs = thead.select('tr')
        for tr in trs:
            if (not tr.has_attr('class')):
                for i in range(10):
                    th = tr.select('th')[i].text
                    th = th.replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
                    columns.append(th)
        data.append(columns)

        tbody = table.select_one('tbody')
        trs = tbody.select('tr')
        # if (tbody == None or trs == None):
        #     return
        for tr in trs:
            tds = tr.select('th')[0].text
            for i in range(10):
                td = tr.select('td')[i].text
                # if (td == None):
                #     return
                td = td.replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'').replace(u',', u'')
                if(td=='-' or td==''):
                    td = '0'
                tds += ('/' + td)
            data.append(tds.split('/'))
    except:
        return

    for i in range(5, 10):
        information = Information(stock=Stock.objects.get(code=code), date=data[0][i], sales=int(data[1][i]), profit=int(data[2][i]))
        information.save()

def information_save(code_list):
    for code in code_list:
        data_save(code)

def information_delete():
    information = Information.objects.all()
    information.delete()

def save_all():
    stock_list = Stock.objects.all()
    for stock in stock_list:
        data_save(stock.code)