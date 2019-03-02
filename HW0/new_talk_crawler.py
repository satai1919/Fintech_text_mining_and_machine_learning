'''
from https://github.com/MiccWan/Political-News-Analysis/blob/master/crawler/new_talk_crawler.ipynb
for homework usage.
'''

import sys
import pickle
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_date(news_block_node):
    date_string = news_block_node.find(class_="news_date").string.split('|')[0][2:-1]
    return(datetime.strptime(date_string, '%Y.%m.%d').strftime('%Y-%m-%d'))
    
def get_title(news_block_node):
    return news_block_node.find(class_="news_title").a.string

def get_link(news_block_node):
    return news_block_node.find(class_="news_title").a.get('href')

def get_content(link):
    r = requests.get(link)
    r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text, 'html.parser')
    article_node = soup.find(itemprop='articleBody')
    article = article_node.get_text()
    return article.replace("\n", "")

def get_news_info(each_news):
    date  = get_date(each_news)
    title = get_title(each_news)
    link  = get_link(each_news)
    content = get_content(link)
    
    info = {'date' : date,
            'title': title,
            'link' : link,
            'content': content}
    return(info)

def get_page_news(page_url):
    r = requests.get(page_url)
    r.encoding = "UTF-8"

    soup = BeautifulSoup(r.text, 'html.parser')
    news_blocks = soup.find_all(class_="news-list-item clearfix ")
    
    news = []
    for each_news in news_blocks:
        try:
            news_info = get_news_info(each_news)
#             print(get_title(each_news))
        except:
#             print('-------{}-------'.format())
            pass

        news.append(news_info)
    return(news)

def get_new_talk_news(from_page=1, end_page=270, url="https://newtalk.tw/news/subcategory/2/政治/"):
    print("page_number from {} to {}".format(from_page, end_page -1))
    data = []
    for page_number in range(from_page, end_page):
        print("page_number: {}".format(page_number))
        data = data + get_page_news( url+str(page_number) )
    
    print('done')
    return(data)


data = get_new_talk_news(from_page=1, end_page=270)