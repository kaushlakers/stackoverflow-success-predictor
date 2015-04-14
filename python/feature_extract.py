import re, cgi
from sklearn.base import BaseEstimator, TransformerMixin

class ColumnSelector(TransformerMixin):
    """ A feature selector for scikit-learn's Pipeline class that returns
        specified columns from a dictionary.
    """
    def __init__(self, key):
        self.key = key

    def transform(self, X, y=None):
        X_transformed=[]
        for x in X:
            X_transformed.append(x[self.key])
        return X_transformed

    def fit(self, X, y=None):
        return self
