"""
Created by Daniel Kwan at 2020-07-01

Description: gets word count of files

"""

import os

def get_count(cont):

    for filename in os.listdir("D:\\SideProjects\webscraper v2\\venv\\Dataset\\{}".format(cont)):
        f = open("D:\\SideProjects\webscraper v2\\venv\\Dataset\\{}\\{}".format(cont,filename), "rt",encoding="utf-8")
        data = f.read()
        words = data.split()

        c = len(words)

        print("\nNumber of words in {} :".format(filename), c)

        if c <= 200:
            f.close()
            os.remove("D:\\SideProjects\webscraper v2\\venv\\Dataset\\{}\\{}".format(cont,filename))
            print("Removed {} due to lack of words".format(filename))
        else:
            f.close()