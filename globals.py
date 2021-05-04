import telebot
from psycopg2_db import DataBase
Token = '1790254613:AAHLvFz4F6V7JRyb_jIsJlyejnMHeeRqfKY'
url = 'https://www.rbc.ru/'
convertion_message = 'Валюты должны быть написаны капслоком и в таком ' \
                     'формате, как они называются на бирже.\nСписок ' \
                     'существующих валют: https://ru.wikipedia.org/wiki/' \
                     '%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%83%D' \
                     '1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%' \
                     'D1%85_%D0%B2%D0%B0%D0%BB%D1%8E%D1%82\n' \
                     'Просто напишите боту сообщение в нужном формате и он все конвертирует.' \
                     'Формат: <количество> <из какой валюты хотите перевести> <в какую валюту хотите перевести>' \
                     'Например: 3 USD RUB'
bot = telebot.TeleBot(Token)
db = DataBase()
mailing_time = "10:00"
