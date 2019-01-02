import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://news.cnyes.com/news/cat/tw_stock')

# print("鉅亨網")
for i in range(1,10):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
soup = BeautifulSoup(driver.page_source)

gihun = []

for index,ele in enumerate(soup.find("div","_2bF theme-list").find_all('a'),0):
    gg_url = "https://news.cnyes.com" + ele.get('href')
    gihun.append(gg_url)
    # gg_url  

i = 0
z1 = open("123456789.txt",'w',encoding = 'utf-8')
for i,gihun_all in enumerate(gihun):  
    res =  requests.get(gihun_all)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.find('span',{'class':'_uo1'}).text
    date = soup.find('time').text
    # z1 = open("123456789.txt",'w',encoding = 'utf-8') #迴圈寫檔案
    # z1 = (%d.txt%(i)) #索引寫入 要加入上面那一行開txt黨
    
    # content = soup.find_all('p')
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    # for content in con:
    #     content = con.get_text()
    # content = str(content)
    if title == None:
        continue
    # elif content == None:
    #     continue
    try:
            # content = item.find('p').text
        for item in soup.find_all('div',{'class':'_1Uu'},limit=1):
            content = item.text
            if content == None:
                continue
        #     # content
            # z1.write('\n')
            # z1.write('鉅亨網')
            # z1.write('\n')
            z1.write(title)
            z1.write('\n')
            # z1.write("日期:"+date)
            # z1.write('\n')
            z1.write(content)
            z1.write('\n')
            # z1.write("網址:"+gihun_all)
            # z1.write('\n')
            # z1.write('===================================================')
            z1.write('\n')
            # # z1.write('=============原始碼===============')
            # # z1.write(single_news_str)
            # z1.write('=======================================================')
    except:
        continue



    