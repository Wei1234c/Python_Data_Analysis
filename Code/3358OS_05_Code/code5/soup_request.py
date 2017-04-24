from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('loremIpsum.html'))

print "First div\n", soup.div
print "First div class", soup.div['class']

print "First dfn text", soup.dl.dt.dfn.text

for link in soup.find_all('a'):
    print "Link text", link.string, "URL", link.get('href')

# Omitting find_all
for i, div in enumerate(soup('div')):
   print i, div.contents


#Div with id=official
official_div = soup.find_all("div", id="official")
print "Official Version", official_div[0].contents[2].strip()

print "# elements with class", len(soup.find_all(class_=True))

tile_class = soup.find_all("div", class_="tile")
print "# Tile classes", len(tile_class)

print "# Divs with class containing tile", len(soup.find_all("div", class_=re.compile("tile")))

print "Using CSS selector\n", soup.select('div.notile')
print "Selecting ordered list list items\n", soup.select("ol > li")[:2]
print "Second list item in ordered list", soup.select("ol > li:nth-of-type(2)")

print "Searching for text string", soup.find_all(text=re.compile("2014"))

