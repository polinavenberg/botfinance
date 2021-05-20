import news
import globals
from globals import bot
from conversion import convert


def create_conversion_message():
    '''Функция создает сообщение с курсами валют, которое отправляется
    пользователям, подписанным на рассылку курсов валют.
    :return: Сформированное сообщение
    '''
    currency_list = ['RUB', 'USD', 'EUR', 'BYN', 'GBP', 'JPY']
    mailing_message = [convert(100, 'RUB', final_currency) for final_currency in currency_list]
    return '\n'.join(mailing_message)


def mailing_news():
    '''
    Функция отправляет сообщение с курсами валют всем пользователям,
    подписанным на рассылку курсов валют.
    '''
    news_dict = news.get_news()
    for user in globals.db.get_news_subscribers(True):
        for key, value in news_dict.items():
            # обращаемся к user id нужного нам пользователя, который находится во второй колонке
            #каждой строки таблицы
            bot.send_message(user[globals.id_index_in_table_line], value)


def mailing_currency():
    '''
    Функция отправляет сообщение с актуальными новостями всем пользователям,
    подписанным на рассылку новостей.
    '''
    for user in globals.db.get_currency_subscribers(True):
        bot.send_message(user[globals.id_index_in_table_line], create_conversion_message())
