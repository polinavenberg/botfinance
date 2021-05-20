import globals
from globals import bot, db
import keyboards
import mailing
import schedule
import time
from multiprocessing.context import Process
from functions import conversion_message, mailing_message, news_message, \
    processing_get_text_message


@bot.message_handler(commands=['start', 'help'])
def base_functions(message):
    '''
    Функция, которая отвечает на основные команды.
    :param message: сообщение пользователя(команда)
    '''
    if message.text == '/start':
        bot.reply_to(message,
                     f'Привет, {message.from_user.first_name}. Я Finance Bot.',
                     reply_markup=keyboards.main_keyboard)
        if not db.check_user_existion(message.chat.id):
            db.add_new_user(message.chat.id)
    elif message.text == '/help':
        bot.send_message(message.chat.id, globals.help_message)


@bot.message_handler(commands=['/news', '/conversion', 'mailing'])
def main_bot_functions(message):
    '''
    Функция, которая отвечает на главные команды бота
    :param message: сообщение пользователя(команда)
    '''
    if message.text == '/news':
        news_message(message.chat.id)
    if message.text == '/conversion':
        conversion_message(message.chat.id)
    if message.text == '/mailing':
        mailing_message(message.chat.id)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    '''
    Функция, которая отвечает на сообщения пользователя.
    :param message: сообщение пользователя
    '''
    processing_get_text_message(message)


def packets_to_host():
    '''
    Функция, которая ведет отсчет времени для рассылки по расписанию.
    '''
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_process():
    '''
    Функция, которая запускает процесс отсчета времени.
    '''
    process = Process(target=packets_to_host, args=())
    process.start()


def schedule_messages():
    '''
    Функция, которая задает время, в которое осуществляется рассылка
    '''
    schedule.every().day.at(globals.mailing_time).do(mailing.mailing_news)
    schedule.every().day.at(globals.mailing_time).do(mailing.mailing_currency)


if __name__ == '__main__':
    start_process()
    bot.polling(none_stop=True)
    schedule_messages()
