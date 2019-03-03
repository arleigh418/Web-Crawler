import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.ptt.cc/bbs/facelift/index.html')

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(1)
print (driver.current_url)



ptt = []
for i in range(0,100):
    # ptt_url = driver.current_url
    print(driver.current_url)
    ptt.append(driver.current_url)
    driver.find_element_by_xpath("//div[@class='btn-group btn-group-paging']/a[2]").click()

f = open('ptt_facelift.txt','w',encoding = 'utf-8')
c = 1
for x in ptt:
    print("===================第",c,"頁===================")
    c = c+1
    ptt_res = requests.get(x)
    soup = BeautifulSoup(ptt_res.text, 'html.parser')
    
    for y in soup.find_all('div','title'):
        title = y.text
        print(title)
  

    


