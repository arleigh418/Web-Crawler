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




ptt = []
for i in range(0,10):
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
                print(url)
        except AttributeError:
                print('url_error')
        try:
                print(title)
        except UnicodeEncodeError:
                print('Unocode_error')

        
        # ptt_url.append(x.select('href'))
count = 1
for g in ptt_url:
    ptt_all = requests.get(g)
    soup_2 = BeautifulSoup(ptt_all.text,'html.parser')
    z = soup_2.select('#main-content')[0].text
    txt_name = "D:/ptt/第"+str(count)+'篇.txt'
    with open(txt_name,'w',encoding = 'utf-8') as f:
            f.write(z)
    f.close()
    print('抓到共',count,'篇')
    count = count+1


    
    
  

    


