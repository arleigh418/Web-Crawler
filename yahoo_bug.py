import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://tw.stock.yahoo.com/news_list/url/d/e/N2.html')
soup = BeautifulSoup(driver.page_source)

yahoo_news = []


for i in range(0,20):
    i+=1
    if i < 21:
        soup = BeautifulSoup(driver.page_source) 
        driver.find_element_by_xpath("//input[@value = '下一頁']").click()
        time.sleep(2)
        for each_item in soup.find(id = "newListTable").find_all("a","mbody"):
         
            if each_item.get('href') != '#':
                yahoo_url = each_item.get('href')
               
                yahoo_news.append(yahoo_url)           
    else:
        break


g1 = open("yahoo_news.txt",'w',encoding = 'utf-8')
for yahoo_all in yahoo_news:
    news = requests.get(yahoo_all)
    single_news = BeautifulSoup(news.text,'html.parser')
    single_news_str = str(single_news)
    
    for yahooo in single_news.find_all('table',{'class':'yui-text-left'},limit=1): #若是沒必要分別存標題、時間等等，可以採用更簡單的方式。

        title = yahooo.find('h1',{'class':'mbody1 style1'}).text
        date =yahooo.find('span',{'class':'t1'}).text
        content = str(yahooo.select('p'))
        content = content.replace('[<p>' , '')
        content = content.replace('</p>]' , '')
        content = content.replace('<br>' , '')
        content = content.replace('<br/>' , '')
        content = content.replace('<p>' , '')
        content = content.replace('</p>' , '')

        g1.write("標題:"+title)
        g1.write(" 日期:"+date)
        g1.write(" 網址:"+yahoo_all)

        g1.write('\n')
        g1.write(content)
        g1.write('\n')
        g1.write('=======================================================')
        g1.write('\n')  
    # except:
    #     continue
        



    
    
    
        

