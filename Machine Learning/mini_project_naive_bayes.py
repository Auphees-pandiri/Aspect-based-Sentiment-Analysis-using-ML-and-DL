import pandas as pd
import numpy as np
import nltk
import string
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords

def load_data(path):
    data = pd.read_csv(path)
    x = data['reviewText'].tolist()
    y = data['sentiment'].tolist()
    return x, y
#train and test
train_x, train_y = load_data('train.csv')
test_x, test_y = load_data('test.csv')

#train data
corpus=[]
for i in range(0,len(train_x)):
    review=re.sub(r'\W',' ',str(train_x[i]))
    review=review.lower()
    review=re.sub(r'\s+[a-z]\s+',' ',review)
    review=re.sub(r'^[a-z]\s+',' ',review)
    review=re.sub(r'\s+',' ',review)
    corpus.append(review)
#test data
corpus1=[]
for i in range(0,len(test_x)):
    review=re.sub(r'\W',' ',str(train_x[i]))
    review=review.lower()
    review=re.sub(r'\s+[a-z]\s+',' ',review)
    review=re.sub(r'^[a-z]\s+',' ',review)
    review=re.sub(r'\s+',' ',review)
    corpus1.append(review)
    
 #train data
from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer(max_features=2000,stop_words=stopwords.words('english'))
X=vectorizer.fit_transform(corpus).toarray()

from sklearn.feature_extraction .text import TfidfTransformer
transformer=TfidfTransformer()
X=transformer.fit_transform(X).toarray() 

#test data
from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer(max_features=2000,stop_words=stopwords.words('english'))
X1=vectorizer.fit_transform(corpus1).toarray()

from sklearn.feature_extraction .text import TfidfTransformer
transformer=TfidfTransformer()
X1=transformer.fit_transform(X1).toarray() 

#train data
for i in range(0,len(train_y)):
    if train_y[i]=='pos':
        train_y[i]=1
    elif(train_y[i]=='neg'):
        train_y[i]=0
        
#test data
for i in range(0,len(test_y)):
    if test_y[i]=='pos':
        test_y[i]=1
    elif(test_y[i]=='neg'):
        test_y[i]=0
        
        
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X, train_y)        
        
pred_y=classifier.predict(X1)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(test_y,pred_y)

print(cm)

a=cm[0][0]+cm[1][1]
b=cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1]
acc=a/b
print("accuracy is",acc)