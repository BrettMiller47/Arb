import webbrowser
from urllib.request import urlopen
import requests
import bs4 as bs4
from bs4 import BeautifulSoup
import lxml
import urllib
import os
import sys
url = "https://sportsbook.draftkings.com/featured?category=game-lines"

urllib.request.urlretrieve(url, "test.txt")

soup = requests.get("https://sportsbook.draftkings.com/featured?category=game-lines").text
print(soup)

body_Tag = soup.find("sportsbook-tabbed-subheader__tabs sportsbook-custom-scrollbar-dark")
print(body_Tag)
#"competitiorType":"Team"
