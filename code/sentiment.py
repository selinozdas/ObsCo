# -*- coding: utf-8 -*-
"""obsco

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VzaJnLiXVwA1HqRZeWWGzK8kgcsBzDlv
"""


"""Import Libraries"""

import keras
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, SpatialDropout1D
from keras.callbacks import ModelCheckpoint
import os
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import nltk

"""Read The Dataset"""

tweets = pd.read_excel(r'C:\Users\Selin\Documents\GitHub\ObsCo\code\tweets.xlsx')
data = tweets[['tweet','tag']]
data = data.sample(frac=1)
data = data[data.tag !='notr']

"""Pre-processing"""

nltk.download('stopwords')
tr_stops = set(nltk.corpus.stopwords.words('turkish'))

data['tweet'] = data['tweet'].apply(lambda x: x.lower())
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ş', 's'))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ı', 'i'))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ğ', 'g'))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ö', 'o'))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ç', 'c'))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ü', 'u'))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('im ', ' '))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('in ', ' '))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ydi', ''))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('ydu', ''))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('imiz', ''))
data['tweet'] = data['tweet'].apply(lambda x: x.replace('umuz', ''))
data['tweet'] = data['tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in tr_stops]))
data['tweet'] = data['tweet'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

print(data[ data['tag'] == 'olumlu'].size)
print(data[ data['tag'] == 'olumsuz'].size)

"""Tokenization"""

max_features = 2000
tokenizer = Tokenizer(num_words = max_features, split = ' ')
tokenizer.fit_on_texts(data['tweet'].values)
X = tokenizer.texts_to_sequences(data['tweet'].values)
X = pad_sequences(X)

"""Neural Network"""

embed_dim = 128

lstm_out = 196

model = Sequential()

model.add(Embedding(max_features, embed_dim))

model.add(Dropout(0.5))

model.add(LSTM(lstm_out, dropout=0.5, recurrent_dropout=0.5))


model.add(Dense(2,activation='softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])

print(model.summary())

"""Declaring Dataset"""

Y = pd.get_dummies(data['tag'].values)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

"""Selecting Some Data for Training and Some for Validation"""

X_val = X_train[:500]
Y_val = Y_train[:500]
partial_X_train = X_train[500:]
partial_Y_train = Y_train[500:]

"""Train the Network"""

batch_size = 512
history = model.fit(partial_X_train, 
                    partial_Y_train, 
                    validation_data=(X_val, Y_val))

eval_test = ['iletisim mukemmel']
labels = ['olumsuz','olumlu']
T = tokenizer.texts_to_sequences(eval_test)
pred = model.predict(T)
weight = 0
def checkpoint(h, k, x, y, a): 
    p =(y-k)**2-4*a*(x - h) 
    if p > 0: 
        print ("Negative\n") 
    elif p == 0: 
        print ("Neutral\n") 
    else: 
        print ("Positive\n")
from sympy import *
def find_distance(x_cor,y_cor):
    x = Symbol('x')
    eqn = -2*(y_cor*(0.00276 - 0.007*x) + x_cor - 0.0000245*x**3 + 0.00002898*x**2 - 0.995808*x - 0.001656)
    return solve(eqn)[0]
    
if len(pred) == 0:
    weight = 0
else:
    x_cor = 0
    y_cor = 0
    size = len(pred)
    print(pred)
    for entry in pred:
        x_cor += entry[0]
        y_cor += entry[1]
    x_cor = x_cor/size
    y_cor = y_cor/size
    dist = find_distance(x_cor,y_cor)
    h= 0.50
    k= 0.45
    checkpoint(h,k,x_cor,y_cor,dist)