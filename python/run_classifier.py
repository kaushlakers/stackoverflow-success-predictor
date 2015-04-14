from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.naive_bayes import *
from sklearn import metrics
from feature_extract import *
from data_parser import *
from utils import *
import numpy as np
def main():
    baseline = Pipeline([('extract', ColumnSelector('Body')),
                          ('vect', CountVectorizer(min_df=5,stop_words='english')),
                          #('tfidf', TfidfTransformer()),
                          ('clf', MultinomialNB())])

    X,y = parse_xml_and_separate_labels('../data/Posts.xml')
    split_index=int(0.75*len(X))
    X_train, y_train = X[0:split_index],y[0:split_index]
    X_test, y_test = X[split_index:],y[split_index:]
    _ = baseline.fit(X_train, y_train)
    predicted = baseline.predict(X_test)
    print str(np.mean(predicted == y_test))
    Utils.write_to_file("report.txt", metrics.classification_report(y_test, predicted)

if __name__ == "__main__":
    main()