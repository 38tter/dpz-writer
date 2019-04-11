# coding: UTF-8
import requests as web
import bs4
import csv
import re
import codecs
from time import sleep
import random

sleep(1)
resp = web.get('https://dailyportalz.jp/kiji/chugoku-shikakui-tatemono')
resp.raise_for_status()

soup = bs4.BeautifulSoup(resp.text, "html.parser")
#share_num = soup.find_all(id="u_0_3")
#share_num = soup.find_all("a")

print(soup.get_text())
#for link in share_num:
  #print(soup.prettify)
  #print(link.get('href'))
#print(share_num)
#text3 = re.search(r"\s[0-9]*\s",text2)

#if text3:
#    print("{0},{1}".format(gengo, text3.group(0)))
#    with open(datpath, mode='a') as f:
#        f.write('\n{0} {1}'.format(gengo, text3.group(0)))
