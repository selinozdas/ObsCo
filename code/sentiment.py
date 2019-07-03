import pandas as pd
import numpy as np
import nltk
import re
import pickle
from util import *
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

data = pd.read_excel(r'C:\Users\Selin\Desktop\nlp\combined.xlsx')
data = data[['content\n','positivity']]
data['content\n'] = data['content\n'].apply(lambda x: x.lower())
data['content\n'] = data['content\n'].apply(lambda x: ''.join(remove_stopwords(x)))
data['content\n'] = data['content\n'].apply(lambda x: ''.join(remove_suffix(x)))
data['content\n'] = data['content\n'].apply(lambda x: ''.join(remove_special_characters(x)))
X_train, X_test, y_train, y_test = train_test_split(data['content\n'], data['positivity'], random_state = 0)

vect = CountVectorizer(encoding ='iso-8859-9').fit(X_train)
X_train_vectorized = vect.transform(X_train)
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
predictions = model.predict(vect.transform(X_test))

feature_names = np.array(vect.get_feature_names())
sorted_coef_index = model.coef_[0].argsort()

vect = TfidfVectorizer(min_df = 5).fit(X_train)

X_train_vectorized = vect.transform(X_train)
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
predictions = model.predict(vect.transform(X_test))

feature_names = np.array(vect.get_feature_names())
sorted_tfidf_index = X_train_vectorized.max(0).toarray()[0].argsort()
vect = CountVectorizer(min_df = 5, ngram_range = (1,2)).fit(X_train)
X_train_vectorized = vect.transform(X_train)


model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
predictions = model.predict(vect.transform(X_test))

feature_names = np.array(vect.get_feature_names())
sorted_coef_index = model.coef_[0].argsort()

filename = 'obsco_model.sav'
joblib.dump(model, open(filename, 'wb'))


