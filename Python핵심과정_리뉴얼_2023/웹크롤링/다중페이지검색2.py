# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

for n in range(0,10):
        data ='https://www.clien.net/service/board/park?&od=T31&po=' + str(n)
        req = urllib.request.Request(data)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html5lib')
        list = soup.findAll('a', attrs={'class':'list-subject'})

        for item in list:
                try:
                        title = item.text
                        if (re.search('아이폰', title)):
                                print(title.strip())
                                print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
