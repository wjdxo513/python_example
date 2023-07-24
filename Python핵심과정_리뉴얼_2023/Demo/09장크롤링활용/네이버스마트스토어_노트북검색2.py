import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

URL = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=price_asc&timestamp=&viewType=list'

driver.get(URL)
#페이지가 전부 로딩될 때까지 대기 시간 필요 
time.sleep(50)

soup = BeautifulSoup(driver.page_source, 'html.parser')
goods_list = soup.select('li.basicList_item__0T9JD')

#가격을 검색하는 경우 
#<span class="price_num__S2p_v" data-testid="SEARCH_PRODUCT_PRICE">300,000원</span>

try: 
    #while구문을 사용해서 작업하는 경우 
    count = len(goods_list)
    i = 0 
    while i<count:
        item_name = goods_list[i].select_one('div.basicList_title__VfX3c > a').get('title')
        item_price = goods_list[i].select_one('span.price_num__S2p_v').text
        print(item_name)
        print(item_price)
        i += 1 
except:
    pass 
