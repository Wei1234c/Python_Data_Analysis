import nltk

sw = set(nltk.corpus.stopwords.words('english'))
print "Stop words", list(sw)[:7]

gb = nltk.corpus.gutenberg
print "Gutenberg files", gb.fileids()[-5:]
text_sent = gb.sents("milton-paradise.txt")[:2]
print "Unfiltered", text_sent

for sent in text_sent:
    filtered = [w for w in sent if w.lower() not in sw]
    print "Filtered", filtered
    tagged = nltk.pos_tag(filtered)
    print "Tagged", tagged 

    words= []

    for word in tagged:
        if word[1] != 'NNP' and word[1] != 'CD':
           words.append(word[0]) 

    print words
