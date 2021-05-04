import globals
import lxml
import requests
from bs4 import BeautifulSoup


def get_news():
    '''
    Функция, которая создает словарь, где ключи -- это заголовки новостей,
    а значения -- ссылки на эти новости. Новости берутся с сайта rbc.ru
    :return: словарь с новостями
    '''
    response = requests.get(globals.url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('a', class_='main__feed__link js-yandex-counter')
    news = {}
    for link in links:
        news[link.text[2:]] = link['href']
    return news
