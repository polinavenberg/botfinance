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
    if currency_from == 'RUB':
        from_rate = 1
    else:
        from_rate = rates[currency_from].value

    if currency_to == 'RUB':
        to_rate = 1
    else:
        to_rate = rates[currency_to].value

    result = round(amount * from_rate / to_rate, 2)
    result_message = f'{str(result)} {currency_to}'
    return result_message
