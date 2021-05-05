import globals
from globals import bot, db
from tests import TestFinanceBot
import keyboards
import mailing
import schedule
import time
from multiprocessing.context import Process
from functions import processing_get_text_mes


@bot.message_handler(commands=['start', 'help'])
def send_hello(message):
    '''
    Функция, которая отвечает на команды.
    :param message: сообщение пользователя
    :return:
    '''
    if message.text == '/start':
        bot.reply_to(message,
                     f'Привет, {message.from_user.first_name}. Я Finance Bot.',
                     reply_markup=keyboards.main_keyboard)
        if not db.check_user_existion(message.chat.id):
            db.add_new_user(message.chat.id)
    elif message.text == '/help':
        bot.send_message(message.chat.id, globals.help_message)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    '''
    Функция, которая отвечает на сообщения пользователя.
    :param message: сообщение пользователя
    :return:
    '''
    processing_get_text_mes(message)


schedule.every().day.at(globals.mailing_time).do(mailing.mailing_news)
schedule.every().day.at(globals.mailing_time).do(mailing.mailing_currency)


def packets_to_host():
    '''
    Функция, которая ведет отсчет времени для рассылки по расписанию.
    :return:
    '''
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_process():
    '''
    Функция, которая запускает процесс отсчета времени.
    :return:
    '''
    process = Process(target=packets_to_host, args=())
    process.start()


TestFinanceBot().test_message_handler()

if __name__ == '__main__':
    start_process()
    bot.polling(none_stop=True)
