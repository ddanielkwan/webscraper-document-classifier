"""
@author Daniel Kwan
@date 2020-06-30

Web scraper for Google
"""
import requests
from bs4 import BeautifulSoup
import functions
#-----------------------------------------------------------------------
url = 'https://google.com/search?q=manga'  # main link to get data
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}  # headers
source = requests.get(url, headers=headers).text  # url source

#making tasty soup
soup = BeautifulSoup(source, 'html.parser')
#-----------------------------------------------------------------------

pages = []

search_div = soup.find_all(class_='rc')  # find all divs tha contains search result
a = (soup.find('div', {'id' : "foot", "role": "navigation"}) )


result = functions.get_result(search_div)



