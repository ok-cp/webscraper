import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image
import re
import os
import urllib.request
import random

URL = "http://bastong.co.kr/"
LIMIT = 2

def extract_pages():

    result = requests.get(URL)    
    html = urlopen(URL)
    bs = BeautifulSoup(html, 'html.parser')
    pagination = bs.find("div", {"class": "pagination"})
    
    ## page numbers
    links = pagination.find_all("a")
    pages = []
    for link in links[1:-1]:
    # for link in links:
        print(link)
        pages.append(int(link.string))

    max_page = pages[-1]
    print(f"MaxPage is {max_page}")
    return max_page


def extract_images(last_page):

    jobs = []
    print(f"Last Page is {last_page}")
    for page in range(last_page):

        print(f"Scrapping page{page}")

        if page == 1:
            html = urlopen(URL)
        else:

        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find("div", {"id": "content"}).find("div", {"class": "reviews_index__body"})
        images = content.find_all('img', {'src':re.compile('.jpg')})

    for image in images: 
        url = 'http:' + image['src'].replace('portrait_','')
        urllib.request.urlretrieve(url, "test{}.jpg".format(random.randrange(1,10000)))

# def  get_jobs_des():

last_page = extract_pages()
extract_images(last_page)



