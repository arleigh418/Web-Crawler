import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time
import pandas as pd
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://news.cnyes.com/news/cat/tw_stock')



# Get scroll height

for i in range(0,20):
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)




soup = BeautifulSoup(driver.page_source)

gihun = []

for index,ele in enumerate(soup.find_all("a","_1Zdp")):
    try:
        gg_url = "https://news.cnyes.com" + ele.get('href')
        gihun.append(gg_url)
    except TypeError:
        print('GET NONE')
        pass

title = []
date = []
content = []
url = []  
non = 0
for i in gihun:
    url.append(i)
    res =  requests.get(i)
    soup = BeautifulSoup(res.text,'html.parser')
    try:
        print('===================================')
        title.append(soup.find('h1').text)
        print(soup.find('h1').text)
        date.append(soup.find('time').text)
        print(soup.find('time').text)
        content.append(soup.find('div',{'class':'_1UuP'}).text)
        
       
    except AttributeError:
        non+=1
        pass
   
print(len(title))
print(len(date))
print(len(content))
pd_store= pd.DataFrame(columns = ['標題','時間','內容','網址'])

pd_store['標題'] = title
pd_store['時間'] = date
pd_store['內容'] = content
pd_store['網址'] = url

pd_store.to_excel('TEST.xlsx')   
print('總爬取網址:',len(gihun))  
print('無效網址:',non)   
