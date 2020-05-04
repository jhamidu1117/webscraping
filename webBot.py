import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=72756'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# print(page.content)
results = soup.find(id='ResultsContainer')
# print(results.prettify())
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    cleaned = title_elem.text.strip()
    print(cleaned)
    cleaned = company_elem.text.strip()
    print(cleaned)
    cleaned = location_elem.text.strip()
    print(cleaned)
    print('\n')
