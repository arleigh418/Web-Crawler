import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


import pandas as pd



url_store = []


for i in range(1,24):
    gg_url = "https://www.ttpia.org.tw/zh-tw/vendor/all?&" + "page={}".format(i)
    # print(gg_url)
    url_store.append(gg_url)

get_url = [] 

for x in url_store:
    res =  requests.get(x)
    soup = BeautifulSoup(res.text)
  
    for i in soup.find('div',{'class':'vendor'}).find_all("a"):
        get_url.append('https://www.ttpia.org.tw'+i.get('href'))

number = []
name = []
boss = []
address = []
phone =[]
phone2 = []
mail = []
url  = []
object_name = []

for h in get_url:
    res2 =  requests.get(h)
    soup2 = BeautifulSoup(res2.text)
    count = 0
    for i in soup2.find_all('div',{'class':'vendor-detail-content'}): 
            if count == 0:
                    number.append(i.text)
                    count+=1
            elif count ==1:
                    name.append(i.text)
                    count+=1
            elif count ==2:
                    boss.append(i.text)
                    count+=1
            elif count ==3:
                    address.append(i.text)
                    count+=1
            elif count ==4:
                    phone.append(i.text)
                    count+=1
            elif count ==5:
                    phone2.append(i.text)
                    count+=1
            elif count ==6:
                    mail.append(i.text)
                    count+=1
            elif count ==7:
                    url.append(i.text)
                    count+=1
            else:
                    object_name.append(i.text)
                    

print('資料處理完畢，存取開始......')
pd_store= pd.DataFrame(columns = ['編號','公司名稱','負責人','地址','電話','傳真','Email','網址','產品'])

pd_store['編號'] = number
pd_store['公司名稱'] = name
pd_store['負責人'] = boss
pd_store['地址'] = address
pd_store['電話'] = phone
pd_store['傳真'] = phone2
pd_store['Email'] = mail
pd_store['網址'] = url
pd_store['產品'] = object_name

pd_store.to_excel('Final.xlsx')   
        
    
    


