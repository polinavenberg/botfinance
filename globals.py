import telebot
from decouple import config
from psycopg2_db import DataBase


Token = config('Token')
url = 'https://www.rbc.ru/'

bot = telebot.TeleBot(Token)
db = DataBase()
mailing_time = "10:00"

rub = 'RUB'
hello_message = 'Привет!'
help_message = 'Привет! Я финансовый бот.\nЧто я могу:\n' \
               '/news: Присылаю 10 актуальных новостей с сайта rbc.ru.\n' \
               '/conversion: Конвертирую любые валюты.\n' \
               '/mailing: Возможность подписаться или ' \
               'отписаться от рассылки новостей и курсов валют.' \
               'Сообщения с рассылкой приходят в 13:00 по московскому ' \
               'времени.'
news_message = 'Держи актуальные новости на сегодня:'
convertion_message = 'Валюты должны быть написаны капслоком и в таком ' \
                     'формате, как они называются на бирже.\nСписок ' \
                     'существующих валют: https://ru.wikipedia.org/wiki/' \
                     '%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%83%D' \
                     '1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%' \
                     'D1%85_%D0%B2%D0%B0%D0%BB%D1%8E%D1%82\n' \
                     'Просто напишите боту сообщение в нужном формате и он все конвертирует.' \
                     'Формат: <количество> <из какой валюты хотите перевести> <в какую валюту хотите перевести>' \
                     'Например: 3 USD RUB'
choose_mailing_message = 'Выберите, на какую рассылку вы хотите подписаться'
choose_action = 'Выберите действие'
success_currency_subscription = 'Вы успешно подписались на рассылку курсов валют.'\
                                ' Теперь каждый день в 13:00 вы будете получать '\
                                'актуальные курсы валют.'
unsuccess_currency_subscription = 'Вы уже были подписаны на рассылку курсов валют'
success_currency_unsubscription = 'Вы успешно отписались от рассылки курсов валют'
unsuccess_currency_unsubscription = 'Вы не были подписаны на рассылку курсов валют'
success_news_subscription = 'Вы успешно подписались на рассылку новостей. '\
                            'Теперь каждый день в 13:00 вы будете получать '\
                            'актуальные новости.'
unsuccess_news_subscription = 'Вы уже были подписаны на рассылку новостей'
success_news_unsubscription = 'Вы успешно отписались от рассылки новостей'
unsuccess_news_unsubscription = 'Вы не были подписаны на рассылку новостей'
back_to_menu = 'Возвращаемся в основное меню'
wrong_message = 'Неправильный ввод'
true_message = '(True,)'
false_message = '(False,)'

user_id = 1; #id пользователя стоит во второй колонке таблицы