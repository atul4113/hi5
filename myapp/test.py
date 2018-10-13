import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from django.shortcuts import render

import csv
base_url =  "https://www.yellowpages.com/menus/los-angeles-ca/pasta?page="
for page in range(1,97,1):
    print(base_url+str(page))
    r = requests.get(base_url+str(page))
    c = r.content

    soup = bs(c,"html.parser")
    all = (soup.prettify())
    data = (soup.find_all("div", {"class": "srp-listing clickable-area mdm"}))

    l = []
    for item in data:
        d = {}
        d["store_name"] = item.find("a", {"class": "business-name"}).text
        try:
            d["adress"] = item.find("span", {"class": "street-address"}).text
        except:
            d["adress"] = None
        try:
            d["locality"] = item.find("span", {"class": "locality"}).text
        except:
            d["locality"] = None
        try:
            d["phone"] = item.find("div", {"class": "phone"}).text
        except:
            d["phone"] = None
        try:
            img = item.find("img")
            d["image"] = img['data-original']
        except TypeError:
            d["image"] = None
        l.append(d)
        import pandas as pd
        df = pd.DataFrame(l)
        print(df)
        df.to_csv('testall.csv')
        print("Done")

