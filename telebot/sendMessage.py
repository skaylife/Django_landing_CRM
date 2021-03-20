import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1) # Получаем значение из бд
        # Записываем значение занисанное в settings из бд / токен chat_id & text
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendmessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'): # Проверка на наличе скобок

            # # Для замены значений в сообщении в телеграм Name = {name} Phone = {phone}
            # Name_l = text.find('{') # Поиск первой скобки name | find ищет с начала строки
            # Name_r = text.find('}') # Поиск второй скобки name | find ищет с начала строки
            # Phone_l = text.rfind('{') # Тоже самое и c phone, | rfind ищет с конца строки
            # Phone_r = text.rfind('}') # Тоже самое и c правой скобкой phone, | rfind ищет с конца строки

            # Используем разрение строки на 3 части
            part_1 = text[0 : text.find('{')] # Разрезаем до первой перемнной {0 :} и псоле первой переменной { 0 : Name_l }
            part_2 = text[text.find('}') + 1 : text.rfind('{')] # + 1 Чтоб продвинуться вперед
            part_3 = text[text.rfind('}') : -1] # От Phone_r и до последнего символа

            # Соеденение всех частей и присвоение в переменную
            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3  # добавление переменных в пустое пространство Name и Phone

        else:
                text_slise = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise
            })
        except:
            pass

        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Все ок сообщение отправлено')
    else:
        pass


