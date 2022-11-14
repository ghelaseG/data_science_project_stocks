# from youtube video https://www.youtube.com/watch?v=q_MWWVgghsQ&list=LL&index=6

import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div',{'class': class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts



def real_time_price(stock_code):
    url = 'https://uk.finance.yahoo.com/quote/' + stock_code + '?p=' + stock_code + '&.tsrc=fin-srch'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, 'My(6px) Pos(r) smartphone_Mt(6px)')
        if texts != []:
            price, change = texts[0], texts[1]
        else:
            price, change = [], []
    except ConnectionError:
        price, change = [], []
    return price, change

Stock = ['TSLA']
print(real_time_price('TSLA'))
