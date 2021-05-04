from multiprocessing.context import Process
import globals
from globals import db
import keyboards
import news
import schedule
import mailing
from conversion import convert
from globals import bot
import time


@bot.message_handler(commands=['start', 'help'])
def send_hello(message):
    if message.text == '/start':
        bot.reply_to(message, f'Привет, {message.from_user.first_name}. Я Finance Bot.', reply_markup=keyboards.main_keyboard)
        if not db.check_user_existion(message.chat.id):
            db.add_new_user(message.chat.id)
    elif message.text == '/help':
        bot.send_message(message.chat.id, f'Ничем не могу помочь')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    message.text.lower()
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text == 'Новости':
        bot.send_message(message.chat.id, f'Держи актуальные новости на сегодня:')
        news_dict = news.get_news()
        for key, value in news_dict.items():
            bot.send_message(message.chat.id, value)
    elif message.text == 'Конвертер валют':
        bot.send_message(message.chat.id, globals.convertion_message)
    elif message.text == 'Подписаться на рассылку':
        bot.reply_to(message, f'Выберите, на какую рассылку вы хотите подписаться',
                     reply_markup=keyboards.subscription_keyboard)
    elif message.text == 'Рассылка новостей':
        bot.send_message(message.chat.id, f'Выберите действие:', reply_markup=keyboards.news_subscription_keyboard)
    elif message.text == 'Подписаться на рассылку новостей':
        if str(db.check_news_subscribtion(message.chat.id)) == '(False,)':
            db.news_subscribe_unsubscribe(message.chat.id, True)
            bot.send_message(message.chat.id, 'Вы успешно подписались на рассылку новостей. Теперь каждый день в 10:00 вы будете получать актуальные новости.', reply_markup=keyboards.subscription_keyboard)
        elif str(db.check_news_subscribtion(message.chat.id)) == '(True,)':
            bot.send_message(message.chat.id, f'Вы уже были подписаны на рассылку новостей', reply_markup=keyboards.subscription_keyboard)
    elif message.text == 'Отписаться от рассылки новостей':
        if str(db.check_news_subscribtion(message.chat.id)) == '(True,)':
            db.news_subscribe_unsubscribe(message.chat.id, False)
            bot.send_message(message.chat.id, 'Вы успешно отписались от рассылки новостей', reply_markup=keyboards.subscription_keyboard)
        else:
            bot.send_message(message.chat.id, 'Вы не были подписаны на рассылку новостей', reply_markup=keyboards.subscription_keyboard)
    elif message.text == 'Рассылка курсов валют':
        bot.send_message(message.chat.id, f'Выберите действие:', reply_markup=keyboards.currency_subscription_keyboard)
    elif message.text == 'Подписаться на рассылку курсов валют':
        if str(db.check_currency_subscribtion(message.chat.id)) == '(False,)':
            db.currency_subscribe_unsubscribe(message.chat.id, True)
            bot.send_message(message.chat.id, 'Вы успешно подписались на рассылку курсов валют. Теперь каждый день в 10:00 вы будете получать актуальные курсы валют.', reply_markup=keyboards.subscription_keyboard)
        else:
            bot.send_message(message.chat.id, 'Вы уже были подписаны на рассылку курсов валют', reply_markup=keyboards.subscription_keyboard)
    elif message.text == 'Отписаться от рассылки курсов валют':
        if str(db.check_currency_subscribtion(message.chat.id)) == '(True,)':
            db.currency_subscribe_unsubscribe(message.chat.id, False)
            bot.send_message(message.chat.id, 'Вы успешно отписались от рассылки курсов валют', reply_markup=keyboards.subscription_keyboard)
        else:
            bot.send_message(message.chat.id, 'Вы не были подписаны на рассылку курсов валют', reply_markup=keyboards.subscription_keyboard)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, f'Возвращаемся в основное меню', reply_markup=keyboards.main_keyboard)
    else:
        try:
            message_list = message.text.split(' ')
            bot.send_message(message.chat.id,
                             convert(int(message_list[0]), message_list[1],
                                     message_list[2]))
        except Exception:
            bot.send_message(message.chat.id, 'Неправильный ввод')


schedule.every().day.at(globals.mailing_time).do(mailing.mailing_news)
schedule.every().day.at(globals.mailing_time).do(mailing.mailing_currency)


def packets_to_host():
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_process():
    p1 = Process(target=packets_to_host, args=())
    p1.start()


if __name__ == '__main__':
    start_process()
    bot.polling(none_stop=True)

