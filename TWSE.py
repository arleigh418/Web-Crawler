#This function just get stock name, stock symbol , foreign investment and securties_investment Net Buy / Net Sell and according to your date.
#If you have other needs, you can modify by yourself.

from bs4 import BeautifulSoup 
from selenium import webdriver
import time
import datetime
from selenium.webdriver.support.select import Select
import pandas as pd

def twse_crawler(start_date:str) -> pd.DataFrame:
    if start_date[4]=='0' : start_month_date = start_date[5]
    else: start_month_date = start_date[4:6]
    
    if start_date[6]=='0':start_day_date = start_date[7]
    else:start_day_date = start_date[6:]
 
    driver = webdriver.Chrome()
    driver.get('https://www.twse.com.tw/zh/page/trading/fund/T86.html')
    time.sleep(2)

    month = Select(driver.find_element_by_name("mm"))
    month.select_by_value(start_month_date)
    time.sleep(2)

    day = Select(driver.find_element_by_name("dd"))
    day.select_by_value(start_day_date)
    time.sleep(2)

    cat_all= Select(driver.find_element_by_name("selectType"))
    cat_all.select_by_value('ALLBUT0999')
    time.sleep(2)

    driver.find_element_by_css_selector("[class='button search']").click()
    time.sleep(5)
    
    cat_all= Select(driver.find_element_by_name("report-table_length"))
    cat_all.select_by_value('-1')
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    name_store, num_store,start_date_store = [],[],[start_date] #存取證券代號&名稱
    foreign_investment_store,securties_investment = [],[] #外資買超&投信買超
    control=0
    for i in soup.find_all('td',{'dt-head-center dt-body-center'}):
        if control ==0:
            num_store.append(i.text)  
            control+=1
        else:
            name_store.append(i.text)
            control = 0

    control = 0
    for i in soup.find_all('td',{'dt-head-center dt-body-right'}):
        if control ==2:
            foreign_investment_store.append(i.text)  
        elif control==8:
            securties_investment.append(i.text)
        control+=1

        if control ==17:
            control=0
        
    data_info = pd.DataFrame()
    
    data_info['Stock Name'] = name_store
    data_info['Stock Num'] = num_store
    data_info['Foreign Investment'] = foreign_investment_store
    data_info['Securties Investment'] = securties_investment
    data_info['Date'] = start_date_store*len(name_store)
    return data_info




twse_crawler('20200221')