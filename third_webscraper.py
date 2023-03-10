'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape (self):
        response = urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.find_all('a'):
            url = tag.get('href')
            if url and 'h' in url:
                print("\n" + url)

the_scraper = Scraper('https://news.google.com/')
the_scraper.scrape()
'''


import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all("a"):
            url = tag.get("href")
            if url and "html" in url:
                print("\n" + url)

Scraper('https://news.google.com/').scrape()