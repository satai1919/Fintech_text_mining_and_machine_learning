'''
from https://github.com/MiccWan/Political-News-Analysis/blob/master/crawler/new_talk_crawler.ipynb
for homework usage.
主要修改 get_new_talk_news()：現在可以透過輸入版面名稱指定要新頭殼新聞中哪一版面的新聞了
'''

import sys
import pickle
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_date(news_block_node):
	'''
	找到新聞中的發布日期，並轉成正確的格式
	'''
    date_string = news_block_node.find(class_="news_date").string.split('|')[0][2:-1]
    return(datetime.strptime(date_string, '%Y.%m.%d').strftime('%Y-%m-%d'))
    
def get_title(news_block_node):
	'''
	找到新聞中的標題
	'''
    return news_block_node.find(class_="news_title").a.string

def get_link(news_block_node):
	'''
	找到新聞的網址
	'''
    return news_block_node.find(class_="news_title").a.get('href')

def get_content(link):
	'''
	找到新聞內文
	'''
    r = requests.get(link)
    r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text, 'html.parser')
    article_node = soup.find(itemprop='articleBody')
    article = article_node.get_text()
    return article.replace("\n", "")

def get_news_info(each_news):
	'''
	對每則新聞做處理，找到需要的資料
	'''
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
	'''
	把需要的新聞搜尋頁碼轉成需要的格式，開始抓取每一連結的新聞內容
	'''
    r = requests.get(page_url)
    r.encoding = "UTF-8"

    soup = BeautifulSoup(r.text, 'html.parser')
    news_blocks = soup.find_all(class_="news-list-item clearfix ")
    
    news = []
    for each_news in news_blocks:
        try:
            news_info = get_news_info(each_news)
        except:
        	#無論因為甚麼緣故失敗，就直接略過
            pass

        news.append(news_info)
    return(news)

def get_new_talk_news(from_page=1, end_page=270, cate="政治"):
    '''
	從指定的起始於結束頁碼之間找尋資料（預設1-269頁）
    '''
    category = {"國際":1, "政治":2, "財經":3, "司法":4, "選舉":13, "社會":14, "中國":7, "遊戲":17, "環保":9, "電競":10, "遊戲":17, "科技":8, "創夢":6, "生活":5, "旅遊":15, "藝文":11, "美食":16, "體育":102, "新奇":103}
    url = "https://newtalk.tw/news/subcategory/" 
    print("page_number from {} to {}".format(from_page, end_page -1))
    data = []
    for page_number in range(from_page, end_page):
        print("page_number: {}".format(page_number))
        #一頁一頁的處理
        data = data + get_page_news( url+str(category[""+cate+""])+"/"+str(cate)+"/"+str(page_number) )
    
    print('done')
    return(data)


data = get_new_talk_news(from_page=1, end_page=270, cate="政治")
