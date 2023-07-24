# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우 
hdr = {'User-agent':'Mozila/5.0 (compatible; MSIE 5.5; Windows NT)'}

for n in range(1,11):
        data ='https://dvdprime.com/g2/bbs/board.php?bo_table=comm&page=' + str(n)
        req = urllib.request.Request(data, \
                                          headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.findAll('span', attrs={'class':'mobile_hide'})

        for item in list:
                try:
                        title = item.find('span').text
                        if (re.search('아이폰', title)):
                                print(title.strip())
                except:
                        pass
        
