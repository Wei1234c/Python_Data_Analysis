import feedparser as fp

rss = fp.parse("http://www.packtpub.com/rss.xml")

print "# Entries", len(rss.entries)

for i, entry in enumerate(rss.entries):
   if "Python" in entry.summary:
      print i, entry.title
      print entry.summary
