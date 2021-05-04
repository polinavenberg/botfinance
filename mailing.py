import news
import globals
from globals import bot
from conversion import convert


def create_conversion_message():
    return '100 RUB\n' + convert(100, 'RUB', 'USD') + '\n' + convert(100, 'RUB', 'EUR') + '\n' + convert(100, 'RUB', 'BYN') + '\n' + convert(100, 'RUB', 'GBP') + '\n' + convert(100, 'RUB', 'JPY')


def mailing_news():
    news_dict = news.get_news()
    for user in globals.db.get_news_subscribers(True):
        for key, value in news_dict.items():
            bot.send_message(user[1], value)


def mailing_currency():
    for user in globals.db.get_currency_subscribers(True):
        bot.send_message(user[1], create_conversion_message())
