#!/usr/bin/env python
# coding: utf-8

# # `WEB SCRAPING` - Latest Cars and their Prices

# In[140]:


import requests
import bs4

res = requests.get('https://www.carwale.com/luxury-cars/')

soup = bs4.BeautifulSoup(res.text, 'html')
modelNames = soup.select('h2 > span')
prices = soup.select('div.leftfloat > div > span.font18')

for i in range(len(prices)):
    print(f'{modelNames[i].getText():{29}}', " ",prices[i].getText())

