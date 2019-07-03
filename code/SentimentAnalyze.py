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
from nltk.corpus import stopwords
from sympy import Symbol,solve
def checkpoint(h, k, x, y, a): 
    p =(y-k)**2-4*a*(x - h) 
    print('p',p)
    if p > 0: 
        return -1 
    elif p == 0: 
        return 0 
    else: 
        return 1


def find_distance(x_cor,y_cor):
    x = Symbol('x')
    eqn = -2*(y_cor*(0.00276 - 0.007*x) + x_cor - 0.0000245*x**3 + 0.00002898*x**2 - 0.995808*x - 0.001656)
    return solve(eqn)[0]

def classify(eval_test):
    
    nltk.download('stopwords')
    tr_stops = set(stopwords.words('turkish'))

    eval_test = eval_test.lower()
    eval_test = eval_test.ljust(len(eval_test))
    eval_test = eval_test.replace('ş', 's')
    eval_test = eval_test.replace('ı', 'i')
    eval_test = eval_test.replace('ğ', 'g')
    eval_test = eval_test.replace('ö', 'o')
    eval_test = eval_test.replace('ç', 'c')
    eval_test = eval_test.replace('ü', 'u')
    eval_test = eval_test.replace('im ', ' ')
    eval_test = eval_test.replace('in ', ' ')
    eval_test = eval_test.replace('ydi', '')
    eval_test = eval_test.replace('ydu', '')
    eval_test = eval_test.replace('imiz', '')
    eval_test = eval_test.replace('umuz', '')
    eval_test = eval_test.replace('di', '')
    eval_test = eval_test.replace('du', '')
    eval_test = eval_test.replace('ti', '')
    eval_test = eval_test.replace('tu', '')

    eval_test = ' '.join([word for word in eval_test.split() if word not in tr_stops])
    eval_test = re.sub('[^a-zA-z0-9\s]','',eval_test)
    eval_test = [eval_test]
    tweets = pd.read_excel(r'C:\Users\Selin\Documents\GitHub\ObsCo\code\tweets.xlsx')
    data = tweets[['tweet','tag']]
    data = data.sample(frac=1)
    data = data[data.tag !='notr']

    data['tweet'] = data['tweet'].apply(lambda x: x.lower())
    data['tweet'] = data['tweet'].apply(lambda x: x.ljust(len(x)+1))
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
    data['tweet'] = data['tweet'].apply(lambda x: x.replace('di', ''))
    data['tweet'] = data['tweet'].apply(lambda x: x.replace('du', ''))
    data['tweet'] = data['tweet'].apply(lambda x: x.replace('ti', ''))
    data['tweet'] = data['tweet'].apply(lambda x: x.replace('tu', ''))
    data['tweet'] = data['tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in tr_stops]))
    data['tweet'] = data['tweet'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

    max_features = 2000
    tokenizer = Tokenizer(num_words = max_features, split = ' ')
    tokenizer.fit_on_texts(data['tweet'].values)
    X = tokenizer.texts_to_sequences(data['tweet'].values)
    X = pad_sequences(X)

    embed_dim = 128
    lstm_out = 196
    model = Sequential()
    model.add(Embedding(max_features, embed_dim))
    model.add(Dropout(0.5))
    model.add(LSTM(lstm_out, dropout=0.5, recurrent_dropout=0.5))
    model.add(Dense(2,activation='softmax'))
    model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])

    Y = pd.get_dummies(data['tag'].values)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 42)
    print(X_train.shape,Y_train.shape)
    print(X_test.shape,Y_test.shape)

    X_val = X_train[:500]
    Y_val = Y_train[:500]
    partial_X_train = X_train[500:]
    partial_Y_train = Y_train[500:]

    batch_size = 512
    model.fit(partial_X_train, partial_Y_train,epochs=5, batch_size=batch_size, validation_data=(X_val, Y_val))


    T = tokenizer.texts_to_sequences(eval_test)
    pred = model.predict(T)
    print(pred)
    if len(pred) == 0:
        print('none')
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
        h= 0.575
        k= 0.5
        print('result',checkpoint(h,k,x_cor,y_cor,dist))

eval_test = 'cok iyi degil'
classify(eval_test)