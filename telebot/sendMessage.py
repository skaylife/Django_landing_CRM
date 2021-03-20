import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1) # Получаем значение из бд
    # Записываем значение занисанное в settings из бд / токен chat_id & text
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendmessage'

    # Для замены значений в сообщении в телеграм Name = {name} Phone = {phone}
    Name_l = text.find('{') # Поиск первой скобки name | find ищет с начала строки
    Name_r = text.find('}') # Поиск второй скобки name | find ищет с начала строки
    Phone_l = text.rfind('{') # Тоже самое и c phone, | rfind ищет с конца строки
    Phone_r = text.rfind('}') # Тоже самое и c правой скобкой phone, | rfind ищет с конца строки

    # Используем разрение строки на 3 части
    part_1 = text[0 : Name_l] # Разрезаем до первой перемнной {0 :} и псоле первой переменной { 0 : Name_l }
    part_2 = text[Name_r + 1 : Phone_l] # + 1 Чтоб продвинуться вперед
    part_3 = text[Phone_r : -1] # От Phone_r и до последнего символа



    # Соеденение всех частей и присвоение в переменную
    text_slise = part_1 + tg_name + part_2 + tg_phone + part_3 # добавление переменных в пустое пространство Name и Phone

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slise
    })

#https://api.telegram.org/bot
# 1780657067:AAHhcfuxU8kb4JDHzG2JGKhzEL_0QAutpHU
# /sendMessage
# ?chat_id=
# -569509289
# &text=Api-Беседа

