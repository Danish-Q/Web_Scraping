from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
url = "https://www.linkedin.com/feed/"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify)
title = soup.title
#print(title.string)
#print(type(title))
#print(type(title.string))
#print(type(soup))
markup = "<p><-- Type of Comments in BeautifulSoup--></p>"
soup2 = BeautifulSoup(markup)
#print(type(soup2.string))
paras = soup.find_all('p')
print(soup.find('p')['class'])
print(soup.find('p'))
