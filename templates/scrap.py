import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://www.bhaskar.com/mp/1")
c = r.content

soup = bs(c,"html.parser")
#all = (soup.prettify())
data = (soup.find_all("div", {"class": "inner-taaja-khabre"}))

#l = []
for item in data:
    #d = {}
    #d["store_name"] = item.find("a", {"class": "business-name"}).text
    #d["adress"] = item.find("span", {"class": "street-address"}).text
    #d["locality"] = item.find("span", {"class": "locality"}).text
    #d["phone"] = item.find("div", {"class": "phone"}).text
    #img = item.find("img")
    #d["image"] = img['data-original']
    news_title = item.find("a",'title')
    for news_title in item:
        print(news_title)
    #print(adress)
    #print(locality)
    #print(phone)
    #print(image)
    #print("  ")

    #l.append(d)
    #import pandas as pd
    #df = pd.DataFrame(l)
    #print(df)
    #df.to_csv('t.csv')