# coding: UTF-8
import  re
import urllib.request
from bs4 import BeautifulSoup


class getSingleStockInfo:
    def __init__(self):
        pass
    def get(num,sum):
        stocknum = str(num).zfill(7)
        if num>600000:
            stocknum = str(num).zfill(7)
        else:
            stocknum = '1'+str(num).zfill(6)
        print("股票代码为"+stocknum)
        url = 'http://quotes.money.163.com/' + stocknum + '.html'
        print("对应的查询页面为"+url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
        req = urllib.request.Request(url,headers=headers,)

        try:
            content = urllib.request.urlopen(req)
        except Exception as e:
            print (e)
            return 0
        soup = BeautifulSoup(content, "html.parser")
        StockInfo = soup.findAll('div',{'class':'stock_info' })
        name = soup.find('h1',{'class':'name'}).contents[1].contents[0].encode('utf-8')
       # print(StockInfo)
        NameEncod = name.decode('UTF-8')
        print(NameEncod)