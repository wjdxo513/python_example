# DemoWebDriver.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import chromedriver_autoinstaller as AutoChrome
import shutil

def selenium_test():
    chrome_ver = AutoChrome.get_chrome_version().split('.')[0]
    path = os.path.join(os.getcwd(),chrome_ver)
    path = os.path.join(path,'chromedriver.exe')
    print(path)
    URL = 'https://nid.naver.com/nidlogin.login'
    driver = webdriver.Chrome(str(path))
    driver.get(url=URL)
    userID = driver.find_elements(By.ID, 'id')[0]
    userPwd = driver.find_elements(By.ID, 'pw')[0]
    userID.send_keys("kim")
    userPwd.send_keys("1234")
    
    while(True):
    	pass

selenium_test() 

#이 부분을 수정한다. 
# driver = set_chrome_driver()
# #driver.implicitly_wait(3)
# driver.get('https://nid.naver.com/nidlogin.login')

# #아래의 코드도 수정됨 
# userID = driver.find_elements(By.ID, 'id')[0]
# userPwd = driver.find_elements(By.ID, 'pw')[0]
# userID.send_keys("kim")
# userPwd.send_keys("1234")

# #로그인버튼 클릭 
# # btn = driver.find_elements(By.ID, 'log.login')
# # btn.click() 
