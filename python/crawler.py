import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.marydeka.com'
        source_code = requests.get(url)
        #What exactly is difference between source_code and plain_text?
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a'):
            href = link.get('href')
            title = link.string #the text 
            print(href)
            print(title)
        page += 1

spider(1)