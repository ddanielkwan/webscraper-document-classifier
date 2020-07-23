import string
from newspaper import Article
import os
from newspaper import Config


path = "D:\\SideProjects\webscraper v2\\venv\\Dataset\\"
def writer(titles,links,cont, config):
    #makes folder if does not exist
    if not os.path.exists(path+ "{}".format(cont)):
        os.mkdir(path +"{}".format(cont))
    else:
        print("already has file")

    for i in range(0, len(titles)):

        #strip title from puncuations and create file with title
        s = titles[i].translate(str.maketrans('', '', string.punctuation))
        f = open(path +"{}\{}.txt".format(cont,s), 'a+', encoding="utf-8")
        #reads site text
        try:
            url1 = links[i]
            article1 = Article(url1,config=config)
            article1.download()
            article1.parse()
            a = article1.text
        #writes to file
            f.write(a)
        except:
            pass
        f.close()

    return

