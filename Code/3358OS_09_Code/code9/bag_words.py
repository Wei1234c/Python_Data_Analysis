import nltk
from sklearn.feature_extraction.text import CountVectorizer

gb = nltk.corpus.gutenberg
hamlet = gb.raw("shakespeare-hamlet.txt")
macbeth = gb.raw("shakespeare-macbeth.txt")

cv = CountVectorizer(stop_words='english')
print "Feature vector", cv.fit_transform([hamlet, macbeth]).toarray()
print "Features", cv.get_feature_names()[:5]
