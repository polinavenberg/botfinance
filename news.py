import globals
import lxml
import requests
from bs4 import BeautifulSoup


def get_news():
    response = requests.get(globals.url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('a', class_='main__feed__link js-yandex-counter')
    news = {}
    for link in links:
        news[link.text[2:]] = link['href']
    return news
