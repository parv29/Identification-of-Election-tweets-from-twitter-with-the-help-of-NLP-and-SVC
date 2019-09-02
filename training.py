import pandas as pd

data=pd.read_csv("shuffled.csv")


from sklearn.model_selection import train_test_split

X = data['[A']
y = data['election']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


# Linear SVC:
text_clf_lsvc = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC()),
])

text_clf_lsvc.fit(X_train, y_train)


predictions = text_clf_lsvc.predict(X_test)

from sklearn import metrics
print(metrics.confusion_matrix(y_test,predictions))


print(metrics.classification_report(y_test,predictions))

print(metrics.accuracy_score(y_test,predictions))

from sklearn.externals import joblib
filename = 'finalized_model.sav'
joblib.dump(text_clf_lsvc, filename)


loaded_model = joblib.load(filename)
result = loaded_model.score(X_test, y_test)
loaded_model.predict(["the next PM will be chosen in in in 2025"]