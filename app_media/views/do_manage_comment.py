import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from ..models import Folder, File


@login_required(login_url='login')
def do_create_comment(request):
    '''Создание комментария к папке/файлу.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_create_comment'})


@login_required(login_url='login')
def do_edit_comment(request):
    '''Изменение комментария к папке/файлу.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_edit_comment'})


@login_required(login_url='login')
def do_delete_comment(request):
    '''Удаление комментария к папке/файлу.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_delete_comment'})


@login_required(login_url='login')
def do_get_comments(request):
    '''Просмотр комментариев.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_get_comments'})
