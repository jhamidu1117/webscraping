import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


class WebShooter:
    def __init__(self):
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


if __name__ == "__main__":
    shooter = WebShooter()
    shooter.web_scope('https://www.wikipedia.org/')
    shooter.web_shoot()
    print(shooter.pages)
