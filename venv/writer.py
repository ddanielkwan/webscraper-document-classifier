import string
from newspaper import Article
import os


def writer(titles,links,cont):
    #makes folder if does not exist
    if not os.path.exists('D:\SideProjects\webscraper v2\venv\Dataset\{}'.format(cont)):
        os.makedirs("D:\SideProjects\webscraper v2\\venv\Dataset\{}".format(cont))


    for i in range(0, len(titles)):

        #strip title from puncuations and create file with title
        s = titles[i].translate(str.maketrans('', '', string.punctuation))
        f = open("D:\SideProjects\webscraper v2\\venv\Dataset\{}\{}.txt".format(cont,s), 'a+', encoding="utf-8")
        #reads site text
        url1 = links[i]
        article1 = Article(url1)
        article1.download()
        article1.parse()
        a = article1.text
        #writes to file
        f.write(a)
        f.close()

    return

