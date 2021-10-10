# ЗАПРОС на вход

import json

from django.contrib import auth
from django.http.response import JsonResponse


def do_in(request):
    # 1 Собрать данные из JSON
    obj = json.loads(request.body)
    print(obj)

    # 2 Организовать данные в переменные
    username = obj['username']
    password = obj['password']

    # 3 Войти в аккаунт
    if (aut := auth.authenticate(request, username=username, password=password)):
        auth.login(request, aut)
        return JsonResponse({'result': 'ok'})

    return JsonResponse({'error': 'login attempt faild'})
