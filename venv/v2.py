"""
@author Daniel Kwan
@date 2020-06-30

Web scraper for Google
"""
import requests
from newspaper import Article
from bs4 import BeautifulSoup
import functions
import string
import nltk
import os
import writer
import fileWordCount



titles = []
links = []
descriptions = []
pagelinks = []
#setting up the soup
#-----------------------------------------------------------------------
url = 'https://google.com/search?q='  # main link to get data
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}  # headers
cont = input("What do you want to Google Search? ")
explore = int(input("How many pages do you want to explore? "))
url = url + cont
source = requests.get(url,headers = headers, auth=('user','pass')).text  # url source

#making tasty soup
soup = BeautifulSoup(source, 'lxml')
#-----------------------------------------------------------------------
page = 1
while page != explore + 1:
    print()
    print('Page {}...'.format(page))
    print('-' * 80)

    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    search_div = soup.find_all(class_='rc')  # find all divs that contains search result
    titles, links, descriptions = functions.get_result(search_div, titles, links, descriptions)


    next_link = soup.select_one('a:contains("Next")')
    if not next_link:
        break

    url = 'https://google.com' + next_link['href']
    page += 1



#-----------------------------------------------------------------------


writer.writer(titles,links,cont) #writes to file

fileWordCount.get_count(cont)



