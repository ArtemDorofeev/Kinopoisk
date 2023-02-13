#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install webdriver_manager')


# In[35]:


import pandas as pd
import numpy as np
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
import csv


# In[10]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[12]:


service = Service(executable_path=ChromeDriverManager().install())


# In[30]:


#driver = webdriver.Chrome(service=service)


# In[32]:


# driver.get(lnk)
# html = driver.page_source


# In[63]:


# Формируем суп-объект

def get_soup(url):    
    driver.get(url)    
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    return soup


# In[64]:


# Извлекаем из soup-объекта название и ссылку с id фильма

def links_parse(row):
    page = []
    time.sleep(5)
    try:
        soup = get_soup(row)
        block_pos = soup.select("div.styles_upper__j8BIs a")
        for i in block_pos:    
            name_pos = i.select_one("div.base-movie-main-info_mainInfo__ZL_u3").get_text()
            link_pos = i.get('href')
            dic = {'name': name_pos, 'link': link_pos}  
            page.append(dic)
    except:
        page = []
    return page


# In[65]:


# ЗАПУСК ПАРСИНГА
# - год меняется в теле ссылки после year--
# - количество страниц пагинации меняется в параметрах цикла range внутри скобок

link = 'https://www.kinopoisk.ru/lists/movies/year--2022/?page={}'
year = []
driver = webdriver.Chrome(service=service) # Открывает новую отдельную вкладку браузера хром от selenium
for i in range(1, 666):
    ln = link.format(i)
    inf = links_parse(ln)
    year.extend(inf)
driver.quit()   # Закрывает отдельную вкладку браузера хром от selenium после выполнения цикла


# In[66]:


# Записываем результаты в датафрейм

df_2022 = pd.DataFrame(year)


# In[75]:


# Прибавляем хвост ссылки к домену

df_2022['links'] = df_2022['link'].apply(lambda x: 'https://www.kinopoisk.ru' + x)
df_2022 = df_2022[['name', 'links']]


# In[76]:


df_2022


# In[77]:


df_2022.to_csv('D:\\Data\\Kinopoisk\\df_2022.csv')


# In[ ]:





# In[ ]:




