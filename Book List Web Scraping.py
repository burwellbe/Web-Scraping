# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

url = requests.get("https://cs.gmu.edu/~hfoxwell/580books.html")

soup = BeautifulSoup(url.content, 'html.parser')
listitems = soup.find_all('li')
listitems

filename = "listofbooks.csv"
f = open(filename, "r+")

headers = "title|author|publisher|release\n"
f.write(headers)

for entry in listitems:
    title = entry.a.booktitle.text
    title = title.replace('\n', ' ')
    title = re.sub(r' +', ' ', title)
    
    author = entry.author.text
    author = author.replace('\n', ' ')
    author = re.sub(r' +', ' ', author)
    
    publisher = entry.publisher.text
    publisher = publisher.replace('\n', ' ')
    publisher = re.sub(r' +', ' ', publisher)
    
    release = entry.release.text
    release = author.replace('\n', ' ')
    release = re.sub(r' +', ' ', release)
    
    f.write(title + "|" + author + "|" + publisher + "|" + release + "\n")
f.close()


