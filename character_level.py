import requests
import re

from simple_settings import LazySettings
from telegram.ext import Updater, CommandHandler

settings = LazySettings('settings.base')
updater = Updater(token=settings.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


class TibiaLevelInfo:

    def process(self):
        start_handler = CommandHandler('start', self.start)
        dispatcher.add_handler(start_handler)

        updater.start_polling()

        tibia_level_handler = CommandHandler('level', self._post_info)
        dispatcher.add_handler(tibia_level_handler)

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def _post_info(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{self._get_info(1)} \n{self._get_info(2)}")

    def _get_info(self, choice):
        if choice == 1:
            headers = settings.base_header.copy()
            headers.update({'cookie': settings.COOKIE_MAIN_ACCOUNT})

            request_data = settings.base_data.copy()
            request_data.update({
                'g-recaptcha-response': settings.CAPTCHA_MAIN_ACCOUNT,
                'account_login': settings.ACCOUNT_MAIN,
                'password_login': settings.PASSWORD_MAIN_ACCOUNT,
            })

        if choice == 2:
            headers = settings.base_header.copy()
            headers.update({'cookie': settings.COOKIE_MAKER})

            request_data = settings.base_data.copy()
            request_data.update({
                'g-recaptcha-response': settings.CAPTCHA_MAKER,
                'account_login': settings.ACCOUNT_MAKER,
                'password_login': settings.PASSWORD_MAKER,
            })

        response = requests.post('https://www.demolidores.com.br/', headers=headers, params=settings.params, data=request_data)
        return self._prepare_request(response)

    def _prepare_request(self, response):
        try:
            info = re.findall(r'- Level ([\d]+)', response.text)
            if len(info) == 2:
                return settings.MAIN_ACCOUNT_CHAR_ONE + info[0] + '\n' + settings.MAIN_ACCOUNT_CHAR_TWO + info[1]
            else:
                return settings.MAKER_ACCOUNT_CHAR_ONE + info[0]

        except IndexError:
            return f'Tem que pegar os cookies novamente no site!'


if __name__ == '__main__':
    tibia_info = TibiaLevelInfo()
    tibia_info.process()
