import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = pickle.load(open('pickle/vectorizer.pickle', 'rb'))
clf = pickle.load(open('pickle/classifier.pickle', 'rb'))

def check_message(message):
    return clf.predict(vectorizer.transform([message]))[0]