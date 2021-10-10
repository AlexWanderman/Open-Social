# ЗАПРОС на регистрацию

import json
import re

from django.contrib import auth
from django.http.response import JsonResponse

from ..models import User


def do_reg(request):
    # 1 Собрать данные из JSON
    obj = json.loads(request.body)
    print(obj)

    # 2 Организовать данные в переменные
    username = obj['username']
    password = obj['password']
    first_name = obj['first_name']
    last_name = obj['last_name']
    name = obj['name']
    about = obj['about']
    birthday = obj['birthday']

    # 3 Проверка данных
    if not re.match(r'[a-zA-Z0-9]{3,33}', username):
        print(f'Not match: {username}')
        return JsonResponse({'result': 'input_error'})

    # Валидация password

    if not re.match(r'[a-zA-Zа-яёА-ЯЁ]{2,20}', first_name):
        print(f'Not match: {first_name}')
        return JsonResponse({'result': 'input_error'})

    if not re.match(r'[a-zA-Zа-яёА-ЯЁ]{2,20}', last_name):
        print(f'Not match: {last_name}')
        return JsonResponse({'result': 'input_error'})

    if not re.match(r'[a-zA-Z0-9]{3,33}', name):
        print(f'Not match: {name}')
        return JsonResponse({'result': 'input_error'})

    # Валидация about
    # Валидация birthday

    # 4 Проверка наличия аккаунта
    if User.objects.filter(username=username).exists():
        print(f'Exist: {name}')
        return JsonResponse({'result': 'exist'})

    # 5 Регистрация
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        name=name,
        about=about,
        birthday=birthday,
    )

    # 6 Вход в аккаунт
    if (aut := auth.authenticate(request, username=username, password=password)):
        auth.login(request, aut)
        return JsonResponse({'result': 'ok'})

    return JsonResponse({'result': 'login_error'})
