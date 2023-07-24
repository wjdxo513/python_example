# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request

#User-Agent를 조작하는 경우 
hdr = {'User-agent':'Mozila/5.0 (compatible; MSIE 5.5; Windows NT)'}

req = urllib.request.Request('http://www.clien.net/cs2/bbs/board.php?bo_table=park', \
                                  headers = hdr)
data = urllib.request.urlopen(req).read()
page = data.decode('utf-8', 'ignore')
soup = BeautifulSoup(page, 'html5lib')
list = soup.findAll('td', attrs={'class':'post_subject'})
title = list[2].find('a').text
print(title)
for item in list:
        try:
                title = item.find('a').text
                print(title)
        except:
                pass
        
