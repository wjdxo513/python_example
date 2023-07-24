from bs4 import BeautifulSoup
import urllib.request

pageNum = 1
while (pageNum<=3):
    url = 'http://www.clien.net/cs2/bbs/board.php?bo_table=park&page=' + str(pageNum)
    print(url)
    response = urllib.request.urlopen(url)
    page = response.read().decode('utf-8', 'ignore')

    soup = BeautifulSoup(page, 'html5lib')
    list = soup.findAll('td', attrs={'class':'post_subject'})
    pageNum += 1
    
    for item in list:
        title = item.find('a').text
        print(title)
    
