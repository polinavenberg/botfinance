from globals import bot
import keyboards
from globals import db
import globals
from conversion import convert
import news


def processing_get_text_mes(message):
    message.text.lower()
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text == 'Новости' or message.text == '/news':
        bot.send_message(message.chat.id,
                         'Держи актуальные новости на сегодня:')
        news_dict = news.get_news()
        for key, value in news_dict.items():
            bot.send_message(message.chat.id, value)
    elif message.text == 'Конвертер валют' or message.text == '/conversion':
        bot.send_message(message.chat.id, globals.convertion_message)
    elif message.text == 'Подписаться на рассылку' or message.text == '/mailing':
        bot.reply_to(message,
                     'Выберите, на какую рассылку вы хотите подписаться',
                     reply_markup=keyboards.subscription_keyboard)
    elif message.text == 'Рассылка новостей':
        bot.send_message(message.chat.id, 'Выберите действие:',
                         reply_markup=keyboards.news_subscription_keyboard)
    elif message.text == 'Подписаться на рассылку новостей':
        news_subscribe_message(message.chat.id)
    elif message.text == 'Отписаться от рассылки новостей':
        news_unsubscribe_message(message.chat.id)
    elif message.text == 'Рассылка курсов валют':
        bot.send_message(message.chat.id, 'Выберите действие:',
                         reply_markup=keyboards.currency_subscription_keyboard)
    elif message.text == 'Подписаться на рассылку курсов валют':
        currency_subscribe_message(message.chat.id)
    elif message.text == 'Отписаться от рассылки курсов валют':
        currency_unsubscribe_message(message.chat.id)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Возвращаемся в основное меню',
                         reply_markup=keyboards.main_keyboard)
    else:
        try:
            message_list = message.text.split(' ')
            bot.send_message(message.chat.id,
                             convert(int(message_list[0]), message_list[1],
                                     message_list[2]))
        except Exception:
            bot.send_message(message.chat.id, 'Неправильный ввод')


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
