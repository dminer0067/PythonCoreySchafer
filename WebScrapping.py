#from ipaddress import summarize_address_range
from bs4 import BeautifulSoup
import requests

with open("Sample.html") as html_file:
    soup = BeautifulSoup(html_file,"lxml")
    
#print(soup.prettify())

for article in soup.find_all("div",class_="article"):
    hline = article.h2.a.text
    #print(article)
    summary = article.p.text

    print(hline)
    print(summary)
    
    print()