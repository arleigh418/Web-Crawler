import requests
from bs4 import BeautifulSoup


all_url = []

for i in range(1,7):
    x = 'https://fanti.dugushici.com/ancient_proses/query?page='+str(i)+'&q%5Bprose_series_id_eq%5D=5'
    all_url.append(x)

real_url = []

for x in all_url:
    request =  requests.get(x)
    content = request.text
    soup = BeautifulSoup(content)
    url  = soup.findAll('a') 
    for link in url:
        href = link.get('href')
        if len(href) < 22 and len(href) >= 20:
            real_url.append(href)
        else:
            pass

real_url.remove('/ancient_proses/query')
real_url.remove('http://qqread.qq.com')
real_url.remove('/ancient_proses/query')
print(real_url)
c= 0
article = []
for link in real_url:
    z = 'https://fanti.dugushici.com//'+str(link)
    request =  requests.get(z)
    content = request.text
    soup = BeautifulSoup(content)
    c +=1
    for i in soup.findAll('div',{'class':'content'}):
        print(i.text)
        article.append(i.text)
with open('Tonsi.txt','w',encoding='utf-8') as f:
    for i in article:
        f.write(i)
        # f.write('\n')
    f.close()
        