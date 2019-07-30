import requests
from bs4 import BeautifulSoup
import re

import json
import time
import pandas as pd
import datetime





def get_newsid(start,old):
    newsid = []
    while (start > 1502207999):
        start = start-2592000 - 86400 
        old = old -2592000 - 86400
        # print(datetime.date.fromtimestamp(start))
        # print(datetime.date.fromtimestamp(old))
    
        for i in range(1,200):
            res = requests.get('https://news.cnyes.com/api/v3/news/category/tw_stock?startAt='+str(old)+'&endAt='+str(start)+'&limit=30&page={}'.format(i))
            try:
                jsonData = json.loads(res.text)
            except:
                continue
        
            try:
                if jsonData['items']['next_page_url'] == '/api/v3/news/category/tw_stock?page=2':
                    continue
                else:
                    soup =  jsonData['items']['data']
            
            except KeyError:
                continue

            for x in soup:
                try:
                    if len(x['summary']) ==0:
                        pass
                    else:
                        # print(x['newsId'])
                        newsid.append(x['newsId'])
                                       
                    
                except TypeError:
                    continue     
    return newsid



def get_content(newsid):
    gihun = []
    title = []
    date_data = []
    content = []
    count = 0
    for i in (newsid):
        gg_url = "https://news.cnyes.com" + "/news/id/{}?exp=a".format(i)
        # print(gg_url)
        gihun.append(gg_url)
    for x in gihun:

        res =  requests.get(x)
        soup = BeautifulSoup(res.text,'html.parser')

        try: 
            title.append(soup.find('h1').text)
   
            date_data.append(soup.find('time').text)
            # print(soup.find('time').text)
            content.append(soup.find('div',{'class':'_1UuP'}).text)
            count +=1
            print('處理了:',(count/len(newsid))*100,'%')
       
        except:
            continue
    return title , date_data , content
    



def storge(title,date,content):
    pd_store= pd.DataFrame(columns = ['標題','時間','內容'])
    pd_store['標題'] = title
    pd_store['時間'] = date
    pd_store['內容'] = content
    pd_store.to_excel('Final.xlsx')   
  
#two years news data , and cause this website can just get a month , so we get a month data for each loop

#a month --> start - old =  2592000

start = 1569599999  #target --> 2019/07/29 + one month
old =  1567007999 

newsid = get_newsid(start,old)

title , date_data , content = get_content(newsid)

storge(title,date_data,content)    
