import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import math

#  specified paths
path = "C:\\Users\\tedma\\Desktop\\mypython\\Data\\"
output_path = "C:\\Users\\tedma\\Desktop\\mypython\\pre_processed_data\\"
vector_path = "C:\\Users\\tedma\\Desktop\\mypython\\vectors\\"


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
    stop_words.append('or')
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\nâ€œâ€™,â€¦ëłóźłóźβシвиноϝοῖνοςգինի0123456789𐀺ɣʷμέθáέῳøéæκρώη"
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
def export_dict():
    directory = routes()
    keys = []
    for key in directory:
        keys.append(key)
    return keys

def tf_idf_vector():
    sec_df = []
    final_df = []
    directory = routes()
    vectorizer = TfidfVectorizer()
    keys = []
    value_set = []
    for i in directory.keys():
        keys.append(i)
    for value in keys:
        value_set.append(directory[value])
    larger_list = []
    for i in directory.keys():
        current = []
        list = []
        if not os.path.exists(vector_path+"{}".format(i)):
            os.mkdir(vector_path+"{}".format(i))
        for j in directory[i]:
            text = ""
            f = open(output_path+"{}\\{}.txt".format(i,j[:-4]), 'r', encoding="utf-8")
            for word in f.read().split():
                text = text + " " + word
            list.append(text)
        larger_list.append(list)
    for j in range(len(larger_list)):
        vectors = []
        df = []
        feature_names = []
        vectors = vectorizer.fit_transform(larger_list[j])
        feature_names = vectorizer.get_feature_names()
        dense = vectors.todense()
        denselist = dense.tolist()
        df = pd.DataFrame(denselist, columns=feature_names)
        rounded_df = df.round(decimals=4)
        aa_label = []
        shape = rounded_df.shape
        if (j == 0):
            for i in range(shape[0]):
                aa_label.append(1)
            print("Category name is : {} \nLabel is : {}".format(keys[0].upper(),1))
        elif (j == 1):
            for i in range(shape[0]):
                aa_label.append(2)
            print("Category name is : {} \nLabel is : {}".format(keys[1].upper(),2))
        else:
            for i in  range(shape[0]):
                aa_label.append(3)
            print("Category name is : {} \nLabel is : {}".format(keys[2].upper(),3))
        rounded_df['aa_label'] = aa_label
        rounded_df.to_csv(vector_path+"{}\\{}_vector.csv".format(keys[j],keys[j]), header=True, index=None, sep=' ', mode='a')
        print()
        print(rounded_df)
        sec_df.append(rounded_df)
    print()
    final_df = pd.concat([sec_df[0], sec_df[1],sec_df[2]], ignore_index=True,sort = True)
    return final_df

#-----------------------------------------------------------------
