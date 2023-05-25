import redis # импортируем библиотеку
import json


red = redis.Redis(
    host='localhost',  # ваш хост, если вы поставили Редис к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
    port='6379',  # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегда разный, поэтому его надо копировать оттуда же, что и host.
    password=''  # для локальной машины пароль не требуется (если вы устанавливали Редис к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
)

dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1'))  # с помощью знакомой нам функции превращаем данные, полученные из кэша обратно в словарь
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание