import pandas as pd
import numpy as np
import sklearn
import nltk
import preprocessor as tp
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

def parse_data(filename):
    training_data = pd.read_csv(filename, index_col=False,  usecols=["Tweet Content", "Category No."]).dropna()
    populationX = training_data["Tweet Content"].to_list()
    populationY = training_data["Category No."].to_list()
    num_of_cats = len(set(populationY))
    trainX, trainY = [], []
    testX, testY = [], []

    for i in range(num_of_cats):
        train_count = 0
        for j in range(len(populationX)):
            if populationY[j] == i:
                if train_count < 20:
                    trainX.append(populationX[j])
                    trainY.append(populationY[j])
                    train_count += 1
                elif train_count >= 20:
                    testX.append(populationX[j])
                    testY.append(populationY[j])
                    train_count += 1
                    if train_count == 25:
                        train_count = 0
                        break
            
    return trainX, trainY, testX, testY

def preprocess(text):
    # remove the hashtags
    text = text.replace("#",'')
    text = text.replace("-", ' ')
    text = text.lower()
    
    # token the url, clean out the emojis
    tp.set_options(tp.OPT.URL)
    text = tp.tokenize(text)
    tp.set_options(tp.OPT.EMOJI)
    text = tp.clean(text)

    # flesh out all punctuation and tokenize words into base form
    text = "".join([char for char in text if char not in string.punctuation])
    text = nltk.word_tokenize(text)

    # # initialize a lemmatizer from sklearn and apply to all words in the given list
    lemmatizer = WordNetLemmatizer()
    lem_text = [lemmatizer.lemmatize(word) for word in text]

    final_text = " ".join([word for word in lem_text])

    return final_text