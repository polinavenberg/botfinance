from telebot import types


main_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
main_keyboard.add(types.KeyboardButton(text='Конвертер валют'))
main_keyboard.add(types.KeyboardButton(text='Новости'))
main_keyboard.add(types.KeyboardButton(text='Подписаться на рассылку'))

subscription_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
subscription_keyboard.add(types.KeyboardButton(text='Рассылка новостей'))
subscription_keyboard.add(types.KeyboardButton(text='Рассылка курсов валют'))
subscription_keyboard.add(types.KeyboardButton(text='Назад'))

news_subscription_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
news_subscription_keyboard.add(types.KeyboardButton(text='Подписаться на рассылку новостей'))
news_subscription_keyboard.add(types.KeyboardButton(text='Отписаться от рассылки новостей'))
news_subscription_keyboard.add(types.KeyboardButton(text='Назад'))

currency_subscription_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
currency_subscription_keyboard.add(types.KeyboardButton(text='Подписаться на рассылку курсов валют'))
currency_subscription_keyboard.add(types.KeyboardButton(text='Отписаться от рассылки курсов валют'))
currency_subscription_keyboard.add(types.KeyboardButton(text='Назад'))




