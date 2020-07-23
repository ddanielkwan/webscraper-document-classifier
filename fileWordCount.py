import os
path = "C:\\Users\\tedma\\Desktop\\mypython\\Data\\"
def get_count(cont):

    for filename in os.listdir(path+"{}".format(cont)):
        f = open(path+"{}\\{}".format(cont,filename), "rt",encoding="utf-8")
        data = f.read()
        words = data.split()

        c = len(words)

        print("\nNumber of words in {} :".format(filename), c)

        if c <= 200:
            f.close()
            os.remove(path+"{}\\{}".format(cont,filename))
            print("Removed {} due to lack of words".format(filename))
        else:
            f.close()
