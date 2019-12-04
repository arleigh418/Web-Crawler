import requests

import pandas as pd
import json
import time

def pchome(keyword,mode,npage):
    if mode =='1':
        method = '&sort=sale/dc'

    elif mode =='2':
        method = '&sort=rnk/dc'
        
    elif mode =='3':
        method = '&sort=prc/dc'

    elif mode =='4':
        method = '&sort=prc/ac'

    elif mode =='5':
        method = '&sort=new/ac'
    
    else:
        print('目前僅支援三種mode，請正確輸入')
        exit()

    content = []
    price = []
    originprice = []
    link = []
    for i in range(0,int(npage)):
        time.sleep(0.5)
        print('Start Catch:',i,'頁')
        url = requests.get(f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keyword}&page={i}'+method)
        jsonData = json.loads(url.text)

        json_use = jsonData['prods']
        for use in range(len(json_use)):
            content.append(json_use[use]['describe'])
            price.append(json_use[use]['price'])
            originprice.append(json_use[use]['originPrice'])
            link.append('https://24h.pchome.com.tw/books/prod/'+str(json_use[use]['Id']))
        
    storage = pd.DataFrame(columns = ['商品名稱','商品價格','商品原始價格','商品連結'])
    storage['商品名稱'] = content
    storage['商品價格'] = price
    storage['商品原始價格'] = originprice
    storage['商品連結'] = link
    storage.to_excel('pc_home_keyword={0}_mode={1}_pagecatch={2}.xlsx'.format(keyword,mode,npage),encoding='utf-8')
    

keyword = input('請輸入關鍵字:')
mode = input('請輸入模式(限1、2、3)，1代表有貨優先(預設)；2代表根據精準度排序；3代表價錢由高至低 ; 4代表價錢由低至高 ; 5代表依照新上市排序:')
page = input('請輸入想抓多少頁:')

pchome(keyword,mode,page)
