# ЗАПРОС на выход

from django.contrib import auth
from django.http.response import JsonResponse


def do_out(request):
    auth.logout(request)

    return JsonResponse({'result': 'ok'})
