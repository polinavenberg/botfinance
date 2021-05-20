import globals
from pycbrf import ExchangeRates


def convert(amount, currency_from, currency_to):
    '''
    Функция, которая конвертирует валюты.
    :param amount: сколько единиц нужно конвертировать
    :param currency_from: валюта, которую нужно конвертировать
    :param currency_to: валюта, в которую нужно конвертировать
    :return: готовое сообщение
    '''
    rates = ExchangeRates()

    from_rate = 1 if currency_from == globals.rub else rates[currency_from].value
    to_rate = 1 if currency_to == globals.rub else rates[currency_to].value

    result = round(amount * from_rate / to_rate, 2)
    result_message = f'{str(result)} {currency_to}'
    return result_message
