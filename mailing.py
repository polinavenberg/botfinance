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
    :return:
    '''
    news_dict = news.get_news()
    for user in globals.db.get_news_subscribers(True):
        for key, value in news_dict.items():
            bot.send_message(user[globals.user_id], value)


def mailing_currency():
    '''
    Функция отправляет сообщение с актуальными новостями всем пользователям,
    подписанным на рассылку новостей.
    :return:
    '''
    for user in globals.db.get_currency_subscribers(True):
        bot.send_message(user[1], create_conversion_message())
