import re, cgi
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

class ColumnSelector(TransformerMixin):
    """ A feature selector for scikit-learn's Pipeline class that returns
        specified columns from a dictionary.
    """
    def __init__(self, keys):
        self.keys = keys

    def transform(self, X, y=None):
        X_transformed=[]
        for x in X:
            if len(self.keys) == 1:
                X_transformed.append(x[self.keys[0]])
            else:
                X_transformed.append(tuple(x[key] for key in self.keys))
        return X_transformed

    def fit(self, X, y=None):
        return self

class TokenizeStemTransformer(TransformerMixin):
    '''
    Takes X of the form [(a1,a2,a3),(b1,b2,b3), ....] where each element is a tuple of strings.
    Returns list where the strings in each tuple element are tokenized and stemmed
    '''
    def transform(self, X, y=None):
        X_transformed = []
        for x in X:
            X_transformed.append(tuple(self.tokenize_and_stem(item) for item in x))
        return X_transformed

    def fit(self, X, y=None):
        return self

    def tokenize_and_stem(self, text):
        tokenizer = RegexpTokenizer(r'[A-Za-z\-]{2,}')
        tokens = tokenizer.tokenize(text)
        good_words = [w for w in tokens if w.lower() not in stopwords.words('english')]
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(w) for w in good_words]
        return stemmed_words
