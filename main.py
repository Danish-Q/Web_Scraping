import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)

# commanly used types of objects :
#print(type(title)) # 1.Tag
#print(type(title.string)) # 2. NavigableString
#print(type(soup)) # 3. BeautifulSoup
#markup = "<p><!-- this is a comment --></p>" # 4. Comment
#soup2 = BeautifulSoup(markup)
#print(type(soup2.string))

# Get the title of the HTML page
title = soup.title
# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)
print(soup.find('p')['class']) # Get first element in the HTML page
print(soup.find('p')) # Get classes of any HTML page
# find all the elements with class lead
print(soup.find_all("p", class_ = "lead"))
# Get the text from the tag/soup
print(soup.find('p').get_text())
print(soup.get_text())
# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# print(anchors)
# Get all the links on the page :
for link in anchors :
    if(link.get('href') != '#') :
        linkText = "http://codewithharry.com" +link.get("href")
        all_links.add(link)
        print(linkText)
log = soup.find(id= '__NEXT_DATA__')
for elem in __NEXT_DATA__.contents:
    print(elem)        