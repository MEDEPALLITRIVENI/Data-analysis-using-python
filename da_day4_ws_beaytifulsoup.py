# -*- coding: utf-8 -*-
"""DA_Day4_WS_BeaytifulSoup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aVsVHjdrdge8grZkaQ_WGDCx4hO55QVY
"""



"""Extracting HTML code from any website

Program flow:

1.Import libraries

2.save the url

3.using requests.get(),accesss the web page

4.using BeaytifulSoup(),access the HTML code
"""

from bs4 import BeautifulSoup
import requests as req

url="https://www.google.com/search?gs_ssp=eJzj4tLP1TdIrrI0Noo3YPTiL87IzEvOSMxTyM0vy0wtBgCBMAlz&q=shinchan+movies&oq=shinchan&gs_lcrp=EgZjaHJvbWUqEggDEC4YQxiDARixAxiABBiKBTIVCAAQABhDGIMBGOMCGLEDGIAEGIoFMhIIARAuGEMYgwEYsQMYgAQYigUyDwgCEAAYQxixAxiABBiKBTISCAMQLhhDGIMBGLEDGIAEGIoFMhIIBBAAGEMYgwEYsQMYgAQYigUyDwgFEAAYQxixAxiABBiKBTIHCAYQABiABDIKCAcQABixAxiABDIMCAgQABhDGIAEGIoFMgwICRAAGEMYgAQYigXSAQoyNjI2MGowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8"
page=req.get(url)
code=BeautifulSoup(page.text,'html')
print(code)

t=code.find('title')
print(t)

print(t.text)

"""#Extracting a table from a web page"""

from bs4 import BeautifulSoup
import requests as req
u="https://www.forbesindia.com/article/explainers/top-10-richest-people-india/85909/1"
p=req.get(u)
b=BeautifulSoup(p.text,'html')
t=b.find('table')
h=t.find_all('th')
heading=[i.text for i in h]
print(heading)

#creating data frame with headings
import pandas as pd
mydf=pd.DataFrame(columns=heading)
print(mydf)
rows=h.find_all('td')
data_act=[i.text for i in rows]
print(data_act)

data_act=[i.text for i in rows]
print(data_act)

df1=pd.DataFrame(columns=['name','rank','nw','comp'])
df1

ind=0
start=0
stop=4
for i in data_act:
  if stop<=40:
    df1.loc[ind]=data_act[start:stop]
    start=start+4
    stop=stop+4
    ind=ind+1
df1

df1.to_csv("df1.csv")