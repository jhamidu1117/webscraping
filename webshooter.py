import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


class WebShooter:
    def __init__(self):
        self.uname = 'hot_jamil'
        self.passwd = 'hottest123'
        self.meta_data = pd.DataFrame.empty
        self.url_targets = []
        self.pages = []
        self.links = []

    def web_scope(self, urls):
        if type(urls) == str:
            self.url_targets.append(urls)

    def web_shoot(self):
        self.pages.append(requests.get(self.url_targets[0]))

        self.web_links(self.pages[0])

    def web_links(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            # print('found the URL: ', a['href'])
            self.links.append(a['href'])

    def web_crawl(self, link):
        pass



if __name__ == "__main__":
    shooter = WebShooter()
    shooter.web_scope('http://127.0.0.1:8000/')
    shooter.web_shoot()
    print(shooter.links)
