import time
from telebot import types
import globals
from globals import bot


class TestFinanceBot:
    def test_message_handler(self):
        '''
        Функция, выдающая ошибку, если не прошли тесты
        :return:
        '''
        msg_help = self.create_text_message('/help')
        msg_mailing = self.create_text_message('/mailing')

        @bot.message_handler(commands=['help'])
        def help_handler(message):
            """
            Тест команды /help
            :param message: входное сообщение
            """
            message.text = globals.help_message

        bot.process_new_messages([msg_help])
        time.sleep(1)
        assert msg_help.text == globals.help_message

        @bot.message_handler(commands=['mailing'])
        def mailing_handler(message):
            """
            Тест команды /mailing
            :param message: входное сообщение
            """
            message.text = globals.choose_mailing_message

        bot.process_new_messages([msg_mailing])
        time.sleep(1)
        assert msg_mailing.text == globals.choose_mailing_message

    @staticmethod
    def create_text_message(text):
        '''
        Функция, которая создает сообщения, которые выводит бот на определенную команду
        :param text: команда
        :return:
        '''
        params = {"text": text}
        chat = types.User(11, False, "test")
        return types.Message(1, None, None, chat, "text", params, "")


TestFinanceBot().test_message_handler()
