import globals
import keyboards
import news
from conversion import convert
from globals import bot, db


def hello(chat_id):
    '''
    Функция, которая отвечает на сообщение "Привет"
    :param chat_id: chat id пользователя
    '''
    bot.send_message(chat_id, globals.hello_message)


def news_message(chat_id):
    '''
    Функция, которая отправляет новости
    :param chat_id: chat id пользователя
    '''
    bot.send_message(chat_id, globals.news_message)
    news_dict = news.get_news()
    for value in news_dict.values():
        bot.send_message(chat_id, value)


def conversion_message(chat_id):
    '''
    Функция, которая отправляет сконвертированные валюты
    :param chat_id: chat id пользователя
    '''
    bot.send_message(chat_id, globals.convertion_message)


def mailing_message(chat_id):
    '''
    Функция, которая отвечает на нажатие кнопки "Подписаться на рассылку"
    :param chat_id: chat id пользователя
    '''
    bot.send_message(chat_id, globals.choose_mailing_message,
                     reply_markup=keyboards.subscription_keyboard)


def news_mailing_message(chat_id):
    '''
    Функция, которая отвечает на сообщение "Рассылка новостей"
    :param chat_id: chat id пользователя
    '''
    bot.send_message(chat_id, globals.choose_action,
                     reply_markup=keyboards.news_subscription_keyboard)


def currency_mailing_message(chat_id):
    '''
    Функция, которая отвечает на сообщение "Рассылка курсов валют"
    :param chat_id:chat id пользователя
    '''
    bot.send_message(chat_id, globals.choose_action,
                     reply_markup=keyboards.currency_subscription_keyboard)


def currency_subscribe_message(chat_id):
    '''
    Функция, которая отвечает на сообщение "Подписаться на рассылку курсов валют"
    :param chat_id: chat id пользователя
    '''
    if str(db.check_currency_subscribtion(chat_id)) == globals.false_message:
        db.currency_subscribe_unsubscribe(chat_id, True)
        bot.send_message(chat_id, globals.success_currency_subscription,
                         reply_markup=keyboards.subscription_keyboard)
    else:
        bot.send_message(chat_id, globals.unsuccess_currency_subscription,
                         reply_markup=keyboards.subscription_keyboard)


def currency_unsubscribe_message(chat_id):
    '''
    Функция, которая отвечает на сообщение "Отписаться от рассылки курсов валют"
    :param chat_id: chat id пользователя
    '''
    if str(db.check_currency_subscribtion(chat_id)) == globals.true_message:
        db.currency_subscribe_unsubscribe(chat_id, False)
        bot.send_message(chat_id, globals.success_currency_unsubscription,
                         reply_markup=keyboards.subscription_keyboard)
    else:
        bot.send_message(chat_id, globals.unsuccess_currency_unsubscription,
                         reply_markup=keyboards.subscription_keyboard)


def news_subscribe_message(chat_id):
    '''
    Функция, которая отвечает на сообщение "Подписаться на рассылку новостей"
    :param chat_id: chat id пользователя
    '''
    if str(db.check_news_subscribtion(chat_id)) == globals.false_message:
        db.news_subscribe_unsubscribe(chat_id, True)
        bot.send_message(chat_id, globals.success_news_subscription,
                         reply_markup=keyboards.subscription_keyboard)
    elif str(db.check_news_subscribtion(chat_id)) == globals.true_message:
        bot.send_message(chat_id, globals.unsuccess_news_subscription,
                         reply_markup=keyboards.subscription_keyboard)


def news_unsubscribe_message(chat_id):
    '''
    Функция, которая отвечает на сообщение "Отписаться от рассылки новостей"
    :param chat_id: chat id пользователя
    '''
    if str(db.check_news_subscribtion(chat_id)) == globals.true_message:
        db.news_subscribe_unsubscribe(chat_id, False)
        bot.send_message(chat_id, globals.success_news_unsubscription,
                         reply_markup=keyboards.subscription_keyboard)
    else:
        bot.send_message(chat_id, globals.unsuccess_news_unsubscription,
                         reply_markup=keyboards.subscription_keyboard)


def back_to_menu(chat_id):
    '''
    Функция, которая возвращает пользователя в основное меню
    :param chat_id: chat id пользователя
    '''
    bot.send_message(chat_id, globals.back_to_menu,
                     reply_markup=keyboards.main_keyboard)


commands = {'привет': hello, 'Новости': news_message,
            'Конвертер валют': conversion_message,
            'Подписаться на рассылку': mailing_message,
            'Рассылка новостей': news_mailing_message,
            'Подписаться на рассылку новостей': news_subscribe_message,
            'Отписаться от рассылки новостей': news_unsubscribe_message,
            'Рассылка курсов валют': currency_mailing_message,
            'Подписаться на рассылку курсов валют': currency_subscribe_message,
            'Отписаться от рассылки курсов валют': currency_unsubscribe_message,
            'Назад': back}


def processing_get_text_message(message):
    '''
    Функция, которая выполняет команду из списка. Если не находит, то пытается
    конвертировать валюту из введенного сообщения, при ошибке выдает сообщение
    "Неправильный ввод"
    :param message:
    '''
    if message.text in commands:
        commands[message.text](message.chat.id)
    else:
        try:
            message_list = message.text.split()
            bot.send_message(message.chat.id,
                             convert(int(message_list[0]), message_list[1],
                                     message_list[2]))
        except Exception:
            bot.send_message(message.chat.id, globals.wrong_message)
