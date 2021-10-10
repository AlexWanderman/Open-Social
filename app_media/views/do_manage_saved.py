import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from ..models import Folder, File


@login_required(login_url='login')
def do_create_saved(request):
    '''Сохранение у себя чужой папки/файла.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_create_saved'})


@login_required(login_url='login')
def do_delete_saved(request):
    '''Удаление у себя чужой папки/файла.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_delete_saved'})
