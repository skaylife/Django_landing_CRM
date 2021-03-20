import requests
from .models import TeleSettings


def sendTelegram():
    settings = TeleSettings.objects.get(pk=1) # Получаем значение из бд
    # Записываем значение занисанное в settings из бд / токен chat_id & text
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendmessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })

#https://api.telegram.org/bot
# 1780657067:AAHhcfuxU8kb4JDHzG2JGKhzEL_0QAutpHU
# /sendMessage
# ?chat_id=
# -569509289
# &text=Api-Беседа

