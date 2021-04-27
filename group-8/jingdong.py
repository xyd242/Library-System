#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
import requests
from lxml import etree
url="https://search.jd.com/Search?keyword=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&wq=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&psort=3&click=0"
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'}
def get_one_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return response.status_code
    except RequestException:
        return None
html = get_one_page(url)
choose=etree.HTML(html)
f = open('jingdong.csv','w',newline='' ,encoding='utf-8-sig')
filedname = ['书名','价格','出版社']
writer = csv.DictWriter(f, fieldnames=filedname)
writer.writeheader()

name = choose.xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/a/em/text()')
print(name)
price = choose.xpath('//*[@id="J_goodsList"]/ul/li/div/div[2]/strong/i/text()')
print(price)
chuban = choose.xpath('//*[@id="J_goodsList"]/ul/li/div/div[6]/a/text()')
print(chuban)
for i in range(10):
        sings= {
            '书名': name[i],
            '价格': price[i],
            '出版社': chuban[i]
        }
        print(sings)
        writer.writerow(sings)

f.close()


# In[ ]:




