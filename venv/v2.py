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
import writer

titles = []
links = []
descriptions = []
pagelinks = []
#setting up the soup
#-----------------------------------------------------------------------
url = 'https://google.com/search?q=hip hop'  # main link to get data
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}  # headers
source = requests.get(url,headers = headers).text  # url source

#making tasty soup
soup = BeautifulSoup(source, 'lxml')
#-----------------------------------------------------------------------


search_div = soup.find_all(class_='rc')  # find all divs    tha contains search result

titles, links, descriptions = functions.get_result(search_div, titles, links, descriptions)


# a = soup.find('table')
# b = soup.find("tr", {'valign':'top'})
#
# for i in b:
#     print(str(i))

#writer.writer(titles,links) writes to file


