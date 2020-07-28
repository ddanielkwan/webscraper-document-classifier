import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import math
import tf_idf
from nltk import pos_tag
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.naive_bayes import GaussianNB

def main():
    tf_idf.preprocess()
    data = tf_idf.tf_idf_vector()
    print("This is the final merged data: ")
    df_shuffled = data.sample(frac=1).reset_index(drop=True)
    data_c = df_shuffled.fillna(0)
    print(data_c)
    y = data_c['aa_label']
    x = data_c.drop(['aa_label'],axis = 1)
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,test_size=0.30)
    # fit the training dataset on the NB classifier

    SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
    SVM.fit(x_train,y_train)
    predictions_SVM = SVM.predict(x_test)
    key = tf_idf.export_dict()
    for y in range(len(y_test)):
        print("Actual {:>5} :   Predicted : {:>5}".format(y_test.iloc[y],predictions_SVM[y]))
    print()
    print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, y_test)*100)
####--------------------------------------------------------------------------------------------############
# Testing of the model
main()
