import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
#  specified paths
path = "D:\\SideProjects\webscraper v2\\venv\\Dataset\\"
output_path = "D:\\SideProjects\\webscraper v2\\venv\\vectorize\\pre_processed_data\\"
vector_path = "D:\\SideProjects\\webscraper v2\\venv\\vectorize\\vectors\\"


# Function returns the names of the text in the dataset
# I will need to make modifications that will allow me to do it for an entire directory
def routes():
    file_dict = {}
    folder_names = []
    for name in os.listdir(path):
        entry_path = os.path.join(path,name)
        if os.path.isdir(entry_path):
            folder_names.append(name)
    for i in folder_names:
        files = []
        for name in os.listdir(path+i):
            file_path = os.path.join(path+i,name)
            if os.path.isfile(file_path):
                files.append(name)
        file_dict[i] = files
    return file_dict


# Initializing the preprocessig steps
# Remove stop words as well as symbols
def stopword_symbol(filename):
    stop_words = stopwords.words('english')
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\nâ€œâ€™,â€¦"
    text = ""
    new_text = ""
    cleaned_text = ""
    f = open(filename,'r',encoding="utf8")
    for word in f.read().split():
        text=text + " " + word.lower()
    for word in text:
        if word not in symbols:
            new_text = new_text + word
    for word in new_text.split():
        if word not in stop_words:
            cleaned_text = cleaned_text + " " + word
    return cleaned_text


# Lematissation
def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    lemmatize_text = ""
    for word in text.split():
        lemmatize_text = lemmatize_text + " " +  lemmatizer.lemmatize(word,pos = "v")
    return lemmatize_text

# Methods implements all the functions in the preprocessing.py file and returns datasets
def preprocess():
    file_dict = routes()
    directory = file_dict.keys()
    slashes = "\\"
    for i in directory:
        name = file_dict[i]
        if not os.path.exists(output_path+"{}".format(i)):
            os.mkdir(output_path+"{}".format(i))
        create_path = path+i+slashes
        for j in name:
            text = stopword_symbol(create_path+j)
            updated_text = lemmatize(text)
            f = open(output_path+"{}\\{}.txt".format(i,j[:-4]), 'a+', encoding="utf-8")
            f.write(updated_text)
    return

# list of text documents

def tf_idf_vector():
    directory = routes()
    keys = []
    larger_set = []
    tf= TfidfVectorizer(use_idf=True)
    for i in directory.keys():
        current = []
        list = []
        for j in directory[i]:
            text = ""
            f = open(output_path+"{}\\{}.txt".format(i,j[:-4]), 'r', encoding="utf-8")
            for word in f.read().split():
                text = text + " " + word
            list.append(text)
        larger_set.append(list)
    for i in directory.keys():
        keys.append(i)
    for j in directory.keys():
        if not os.path.exists(vector_path+"{}".format(j)):
            os.mkdir(vector_path+"{}".format(j))
    for i in range(len(larger_set)):
        tfidf_wm = tf.fit_transform(larger_set[i])
        df = pd.DataFrame(tfidf_wm[0].T.todense(), index=tf.get_feature_names(), columns=["TF-IDF"])
        df = df.sort_values('TF-IDF', ascending=False)
        f = open(vector_path+"{}\\{}_vector.txt".format(keys[i],keys[i]), 'a+', encoding="utf-8")
        f.write(df.to_string())

#-----------------------------------------------------------------

preprocess()
tf_idf_vector()
