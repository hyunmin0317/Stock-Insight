import pandas as pd
# from .models import Stock, Information
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# def stock_save():
#     data = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
#     data = data[['회사명', '종목코드']]
#     data = data.rename(columns={'회사명': 'name', '종목코드': 'code'})
#     data.code = data.code.map('{:06d}'.format)
#
#     for n in data.name:
#         stock = Stock(name=n, code=data.query("name=='{}'".format(n))['code'].to_string(index=False))
#         stock.save()
#
# def stock_delete():
#     stock = Stock.objects.all()
#     stock.delete()

def data_save(code):
    URL = 'https://finance.naver.com/item/main.nhn?code='+code
    data = []
    columns = ['주요재무정보']
    source_code_from_URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(source_code_from_URL), 'lxml', from_encoding='UTF-8')
    table = soup.find('table', {'class': 'tb_type1 tb_num tb_type1_ifrs'})
    tbody = table.select_one('tbody')
    trs = tbody.select('tr')
    for tr in trs:
        tds = tr.select('th')[0].text
        for i in range(10):
            td = tr.select('td')[i].text
            td = td.replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
            tds += ('/' + td)
        data.append(tds.split('/'))

    print(data[0][5])
    print(data[0][9])
    print(data[1][5])
    print(data[1][9])

# def data_save(name):
#     information = Information(stock=Stock.objects.get(name=name), date=2021.06, sales=500, profit=100)
#     information.save()

data_save('005930')