import requests
from bs4 import BeautifulSoup
import pandas as pd

def shopee_scraper(keyword,mode,n_page,used=False,new=False):
    if mode =='1':
        method = '&sortBy=relevancy'

    elif mode =='2':
        method = '&sortBy=ctime'
        
    elif mode =='3':
        method = '&sortBy=sales'
        
    else:
        print('目前僅支援三種mode，請正確輸入')
        exit()
    
    headers = {
        'User-Agent': 'Googlebot',
        'From': 'YOUR EMAIL ADDRESS'
    }
    content_store = []
    price_store = []
    link_store = []
    for i in range(0,int(n_page)):
        url  = f'https://shopee.tw/search?keyword={keyword}&page={i}' + method
        print('Start Catch:',i,'頁')
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        contents = soup.find_all("div", class_="_1NoI8_ _2gr36I")
        prices = soup.find_all("span", class_="_341bF0")
        all_items = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
        links = [i.find('a').get('href') for i in all_items]
        
        for c, p, l in zip(contents, prices, links):
            content_store.append(''.join(c.contents[0]))
            price_store.append(str(p.contents[0]))
            link_store.append('https://shopee.tw/'+str(l))
    storage = pd.DataFrame(columns = ['商品名稱','商品價格','商品連結'])
    storage['商品名稱'] = content_store
    storage['商品價格'] = price_store
    storage['商品連結'] = link_store
    
    storage.to_excel('shopee_keyword={0}_mode={1}_pagecatch={2}.xlsx'.format(keyword,mode,n_page),encoding='utf-8')
    
        

keyword = input('請輸入關鍵字:')
mode = input('請輸入模式(限1、2、3)，1代表根據最相關排序；2代表根據最新排序；3代表根據最熱銷排序:')
page = input('請輸入想抓多少頁:')

shopee_scraper(keyword,mode,page)