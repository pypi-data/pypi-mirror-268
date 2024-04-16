#%%
import sqlite3
import time
from bs4 import BeautifulSoup
from helium import *
import pandas as pd
import wansuite as ws
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Date, DateTime, Time, Float
from wansuite import msql, investing
import numpy as np
import re
#%%
ccount = 0
start = False
newspages = {}
newspages["economy"] = "https://www.investing.com/news/economy"
newspages["stock"] = "https://www.investing.com/news/stock-market-news"
newspages["commodity"] = "https://www.investing.com/news/commodities-news"
newspages["currency"] = "https://www.investing.com/news/forex-news"
newspages["indicator"] = "https://www.investing.com/news/economic-indicators"
newspages["world"] = "https://www.investing.com/news/world-news"
newspages["politics"] = "https://www.investing.com/news/politics"
#%%
for m in newspages.keys():
    links = ["https://www.investing.com/news/stock-market-news/a-second-kobayashi-pharma-japan-factory-inspected-over-deaths-3358582"]
    print(m)
    for t in range(1, 2, 1):  # 200
        url = newspages[m] + "/" + str(t)
        print(url)
        start_chrome(url, headless=True)
        print(t)
        # Assuming `news` is a Selenium WebElement containing the HTML of the news article container
        soup = BeautifulSoup(news.get_attribute('innerHTML'), 'html.parser')

        # Use the correct CSS selector to find the <a> tag with the article link
        for link in soup.select('a[data-test="article-title-link"]'):
            links.append(link.get('href'))

        for news in find_all(S('.largeTitle')):
            print(news)
            try:
                soup = BeautifulSoup(news.web_element.get_attribute('innerHTML'), 'html.parser')
                for link in soup.find_all('a'):
                    links.append(link.get('href'))
            except:
                # Element went stale. Retry the operation.
                continue
        kill_browser()
        print(links)
    links = list(set(links))
    links = [x for x in links if x[-8:] != "comments"]
    print("need to update", n, len(links))
    for k in links:
        df = pd.DataFrame(columns=["datetime", "title", "article", "link", "label", "domain"])
        lin = k

        try:
            url0 = "investing.com" + lin
            print(url0)
            start_chrome(url0, headless=True)
            left_columns_html = get_driver().execute_script('return document.getElementById("leftColumn").innerHTML')
            soup = BeautifulSoup(left_columns_html, 'html.parser')

            # Extract the span, p, and h1 elements
            spans = soup.find_all('span')
            ps = soup.find_all('p')
            h1s = soup.find_all('h1', class_='articleHeader')
            article = soup.find_all('div', class_='WYSIWYG articlePage')
            kill_browser()
            cleanarticle = []
            for ar in article:
                cleanarticle.append(ar.get_text())
            news = cleanarticle[0].split("\n\n")[-1]

            title = ""
            author = ""
            resource = ""
            article = ""
            domain=m

            datetime = ""
            label = ""
            cleanspans = []
            for p in spans:
                cleanspans.append(p.get_text())
            for hh in cleanspans:
                if "Published" in hh:
                    datetime = hh
                    break
            if datetime == "":
                spans = soup.find_all('span')
                for p in spans:
                    cleanspans.append(p.get_text())
                for hh in cleanspans:
                    if "Published" in hh:
                        datetime = hh
                        break

            #             temp=re.findall(r'\((.*?)\)', cleanspans[0])
            #             if len(temp)==0:
            #                 datetime= cleanspans[0]
            #             else:
            #                  datetime=temp[-1]

            for h1 in h1s:
                title = h1.get_text()

            cleanps = []
            for p in ps:
                cleanps.append(p.get_text())

            df.loc[len(df)] = [datetime, title, news, url, label,domain]
            if ccount == 0:
                msql.df2table("media", df, "investing_com_news", "append")
                ccount = ccount + 1


        except:
            print("cannot get article", m, " ", lin)

            pass
        try:
            kill_browser()
        except:
            pass

