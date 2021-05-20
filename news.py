import globals
import requests
from bs4 import BeautifulSoup


def get_news():
    '''
    Функция, которая создает словарь, где ключи -- это заголовки новостей,
    а значения -- ссылки на эти новости. Новости берутся с сайта rbc.ru
    :return: словарь с новостями
    '''
    response = requests.get(globals.url)  # отправляю запрос сайту
    soup = BeautifulSoup(response.text, 'lxml')  # получаю http текст страницы
    # в тексте страницы нахожу все заголовки и ссылки на актуальные новости, которые
    # находятся в классе main__feed__link js-yandex-counter
    links = soup.find_all('a', class_='main__feed__link js-yandex-counter')
    # создаю словарь и в его ключи записываю заголовки новостей, а в значения ссылки на новости
    news = {link.text[globals.without_first_two_symbols:]: link['href'] for link in links}
    return news


print(get_news())
