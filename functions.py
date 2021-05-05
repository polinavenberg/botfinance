from globals import bot
import keyboards
from globals import db
import globals
from conversion import convert
import news


def hello(chat_id):
    bot.send_message(chat_id, 'Привет!')


def news_message(chat_id):
    bot.send_message(chat_id,
                     'Держи актуальные новости на сегодня:')
    news_dict = news.get_news()
    for key, value in news_dict.items():
        bot.send_message(chat_id, value)


def conversion_message(chat_id):
    bot.send_message(chat_id, globals.convertion_message)


def mailing_message(chat_id):
    bot.send_message(chat_id,
                     'Выберите, на какую рассылку вы хотите подписаться',
                     reply_markup=keyboards.subscription_keyboard)


def news_mailing_message(chat_id):
    bot.send_message(chat_id, 'Выберите действие:',
                     reply_markup=keyboards.news_subscription_keyboard)


def currency_mailing_message(chat_id):
    bot.send_message(chat_id, 'Выберите действие:',
                     reply_markup=keyboards.currency_subscription_keyboard)


def currency_subscribe_message(chat_id):
    if str(db.check_currency_subscribtion(chat_id)) == '(False,)':
        db.currency_subscribe_unsubscribe(chat_id, True)
        bot.send_message(chat_id,
                         'Вы успешно подписались на рассылку курсов валют.'
                         ' Теперь каждый день в 10:00 вы будете получать '
                         'актуальные курсы валют.',
                         reply_markup=keyboards.subscription_keyboard)
    else:
        bot.send_message(chat_id,
                         'Вы уже были подписаны на рассылку курсов валют',
                         reply_markup=keyboards.subscription_keyboard)


def currency_unsubscribe_message(chat_id):
    if str(db.check_currency_subscribtion(chat_id)) == '(True,)':
        db.currency_subscribe_unsubscribe(chat_id, False)
        bot.send_message(chat_id,
                         'Вы успешно отписались от рассылки курсов валют',
                         reply_markup=keyboards.subscription_keyboard)
    else:
        bot.send_message(chat_id,
                         'Вы не были подписаны на рассылку курсов валют',
                         reply_markup=keyboards.subscription_keyboard)


def news_subscribe_message(chat_id):
    if str(db.check_news_subscribtion(chat_id)) == '(False,)':
        db.news_subscribe_unsubscribe(chat_id, True)
        bot.send_message(chat_id,
                         'Вы успешно подписались на рассылку новостей. '
                         'Теперь каждый день в 10:00 вы будете получать '
                         'актуальные новости.',
                         reply_markup=keyboards.subscription_keyboard)
    elif str(db.check_news_subscribtion(chat_id)) == '(True,)':
        bot.send_message(chat_id,
                         'Вы уже были подписаны на рассылку новостей',
                         reply_markup=keyboards.subscription_keyboard)


def news_unsubscribe_message(chat_id):
    if str(db.check_news_subscribtion(chat_id)) == '(True,)':
        db.news_subscribe_unsubscribe(chat_id, False)
        bot.send_message(chat_id,
                         'Вы успешно отписались от рассылки новостей',
                         reply_markup=keyboards.subscription_keyboard)
    else:
        bot.send_message(chat_id,
                         'Вы не были подписаны на рассылку новостей',
                         reply_markup=keyboards.subscription_keyboard)


def back(chat_id):
    bot.send_message(chat_id, 'Возвращаемся в основное меню',
                     reply_markup=keyboards.main_keyboard)


commands = {'привет': hello, 'Новости': news_message, '/news': news_message,
            'Конвертер валют': conversion_message,
            '/conversion': conversion_message,
            'Подписаться на рассылку': mailing_message,
            '/mailing': mailing_message,
            'Рассылка новостей': news_mailing_message,
            'Подписаться на рассылку новостей': news_subscribe_message,
            'Отписаться от рассылки новостей': news_unsubscribe_message,
            'Рассылка курсов валют': currency_mailing_message,
            'Подписаться на рассылку курсов валют': currency_subscribe_message,
            'Отписаться от рассылки курсов валют': currency_unsubscribe_message,
            'Назад': back}


def processing_get_text_mes(message):
    if message.text in commands:
        commands[message.text](message.chat.id)
    else:
        try:
            message_list = message.text.split(' ')
            bot.send_message(message.chat.id,
                             convert(int(message_list[0]), message_list[1],
                                     message_list[2]))
        except Exception:
            bot.send_message(message.chat.id, 'Неправильный ввод')
