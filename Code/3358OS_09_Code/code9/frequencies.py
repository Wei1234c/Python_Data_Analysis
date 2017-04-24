import nltk
import string


gb = nltk.corpus.gutenberg
words = gb.words("shakespeare-caesar.txt")

sw = set(nltk.corpus.stopwords.words('english'))
punctuation = set(string.punctuation)
filtered = [w.lower() for w in words if w.lower() not in sw and w.lower() not in punctuation]

fd = nltk.FreqDist(filtered)
print "Words", fd.keys()[:5]
print "Counts", fd.values()[:5]
print "Max", fd.max()
print "Count", fd['d']

fd = nltk.FreqDist(nltk.bigrams(filtered))
print "Bigrams", fd.keys()[:5]
print "Counts", fd.values()[:5]
print "Bigram Max", fd.max()
print "Bigram count", fd[('let', 'vs')]
