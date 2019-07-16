#Autor :  Arleigh Chaing

import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time

from collections import Counter
import pandas as pd

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.ptt.cc/bbs/movie/index.html')





ptt = []
for i in range(0,14): 
    # ptt_url = driver.current_url
    print(driver.current_url)
    ptt.append(driver.current_url)
    driver.find_element_by_xpath("//div[@class='btn-group btn-group-paging']/a[2]").click()


c = 1
ptt_url = []
for x in ptt:
    print("===================第",c,"頁===================")
    c = c+1
    ptt_res = requests.get(x)
    soup = BeautifulSoup(ptt_res.text, 'html.parser')
    for y in soup.find_all('div','title'):
        try:
                title = y.text
                url = y.find('a').get('href')
                ptt_url.append('https://www.ptt.cc'+url)
                # print(url)
        except AttributeError:
                print('該篇文章已刪除')
        try:
                print(title)
        except UnicodeEncodeError:
                print('Unocode_error')

        
        # ptt_url.append(x.select('href'))
count = 1
author_store = [] 
title_store = []
date_store = []
articles_store = []
record = 1
for g in ptt_url:
    ptt_all = requests.get(g)
    soup_2 = BeautifulSoup(ptt_all.text,'html.parser')
    z = soup_2.find(id="main-content")
    metas = z.select('div.article-metaline')
    try:
        author = metas[0].select('span.article-meta-value')[0].text
        title = metas[1].select('span.article-meta-value')[0].text 
        date = metas[2].select('span.article-meta-value')[0].text

        author_store.append(author)
        title_store.append(title)
        date_store.append(date)

        articles = soup_2.select('#main-content')[0].text
        articles = articles.replace(author,'')
        articles = articles.replace(title,'')
        articles = articles.replace(date,'')
        articles = articles.replace('作者看板movie標題時間','')
        articles = articles.replace(" ", "")
        articles = articles.replace('\n', "")
        # print(articles)
        articles = re.sub(r'[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a a-zA-Z0-9]','',articles)
        r1 = '[a-zA-Z0-9’!"#$%&\'()(\)|※*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~─]+'
       
        articles_store.append(re.sub(r1, '', articles))
        print('處理了',record,'篇文章')
        record+=1
    except IndexError:
            pass

        
         

pd_store= pd.DataFrame(columns = ['作者','標題','時間','內容'])
pd_store['作者'] = author_store
pd_store['標題'] = title_store
pd_store['時間'] = date_store
pd_store['內容'] = articles_store


pd_store.to_excel('Final.xlsx')
