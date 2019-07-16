import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time
import pandas as pd

start = 4084500 #(2017/04)
end   = 4359000 #(2019/07)
non = 0
correct = 0
gihun = [] 
title = []
date = []
content = []
url = []

for i in range(start,end):
    gg_url = "https://news.cnyes.com" + "/news/id/{}?exp=a".format(i)
    # print(gg_url)
    gihun.append(gg_url) 

count = 0
for i in gihun:
    res =  requests.get(i)
    soup = BeautifulSoup(res.text,'html.parser')
    try:
        count+=1
        if soup.find('h1').text =='404':
            non+=1
            pass
        else:
            title.append(soup.find('h1').text)
            url.append(i)
   
            date.append(soup.find('time').text)
      
            content.append(soup.find('div',{'class':'_1UuP'}).text)
            correct+=1
            print('處理了:',(count/(end-start))*100,'%')
        
            print('錯誤網址 : ',non ,'| 正確網址 : ',correct)
            print('\n')
       
    except AttributeError:
       
        non+=1
        count+=1
        print('處理了:',(count/(end-start))*100,'%')
        
        print('錯誤網址 : ',non ,'| 正確網址 : ',correct)
        print('\n')
        pass
   
print(len(title))
print(len(date))
print(len(content))
print(len(url))

pd_store= pd.DataFrame(columns = ['標題','時間','內容','網址'])

pd_store['標題'] = title
pd_store['時間'] = date
pd_store['內容'] = content
pd_store['網址'] = url

pd_store.to_excel('Final.xlsx')   
print('總爬取網址:',len(gihun))  
print('無效網址:',non)   
    
    
