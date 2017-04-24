import nltk
import string
import random


sw = set(nltk.corpus.stopwords.words('english'))
punctuation = set(string.punctuation)

def word_features(word):
   return {'len': len(word)}

def isStopword(word):
    return word in sw or word in punctuation

gb = nltk.corpus.gutenberg
words = gb.words("shakespeare-caesar.txt")

labeled_words = ([(word.lower(), isStopword(word.lower())) for word in words])
random.seed(42)
random.shuffle(labeled_words)
print labeled_words[:5]

featuresets = [(word_features(n), word) for (n, word) in labeled_words]
cutoff = int(.9 * len(featuresets))
train_set, test_set = featuresets[:cutoff], featuresets[cutoff:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print "'behold' class", classifier.classify(word_features('behold'))
print "'the' class", classifier.classify(word_features('the'))

print "Accuracy", nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(5)
