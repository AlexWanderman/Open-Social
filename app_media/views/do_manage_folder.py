import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from ..models import Folder, ImageFolder, VideoFolder, MusicFolder, PodcastFolder, DocumentFolder

TYPED_FOLDER = {
    'image': ImageFolder,
    'video': VideoFolder,
    'music': MusicFolder,
    'podcast': PodcastFolder,
    'document': DocumentFolder,
}


@login_required(login_url='login')
def do_create_folder(request):
    ''' Создание папки.
        * type - тип папки;
        * name - название;
        * about - описание;
        * -> 'result': 'ok'
        * -> id - id новой папки.
    '''
    obj = json.loads(request.body)
    print(obj)

    user = request.user

    try:
        type = obj['type']
        name = obj['name']
        about = obj['about']
    except KeyError:
        return JsonResponse({'status': 'key error'})

    if type not in TYPED_FOLDER:
        return JsonResponse({'status': 'wrong type'})

    typed_folder = TYPED_FOLDER[type]

    folder = Folder.objects.create(
        user=user,
        name=name,
        about=about,
    )
    folder.save()

    image_folder = typed_folder.objects.create(
        folder=folder,
    )
    image_folder.save()

    return JsonResponse({'status': 'ok', 'id': folder.id})


@login_required(login_url='login')
def do_edit_folder(request):
    ''' Редактирование папки.
        * type - тип папки;
        * id - id папки;
        * name - новое название или null;
        * about - новое описание или null;
        * -> 'result': 'ok'.
    '''
    obj = json.loads(request.body)
    print(obj)

    user = request.user

    try:
        type = obj['type']
        id = obj['id']
        name = obj['name']
        about = obj['about']
    except KeyError:
        return JsonResponse({'error': 'key error'})

    if type not in TYPED_FOLDER:
        return JsonResponse({'error': 'wrong type'})

    typed_folder = TYPED_FOLDER[type]
    folder = typed_folder.objects.get(id=id, user=user)

    if not folder:
        return JsonResponse({'error': 'folder not found'})

    folder.name = name or folder.name
    folder.about = about or folder.about
    folder.save()

    return JsonResponse({'result': 'ok'})


@login_required(login_url='login')
def do_delete_folder(request):
    ''' Удаление папки.
        * id - id папки;
        * -> 'result': 'ok'.
    '''
    obj = json.loads(request.body)
    print(obj)

    if 'id' not in obj:
        return JsonResponse({'error': 'key error'})

    user = request.user
    id = obj['id']

    folder = Folder.objects.get(id=id, user=user)

    if not folder:
        return JsonResponse({'error': 'folder not found'})

    folder.delete()

    return JsonResponse({'result': 'ok'})


@login_required(login_url='login')
def do_get_folders(request):
    ''' Получение списка папок.
        * type - тип папок;
        * page - номер страницы;
        * size - размер страницы;
        * -> 'status': 'ok' или ошибка;
        * -> 'folders': [...]
    '''
    obj = json.loads(request.body)
    print(obj)

    user = request.user

    try:
        type = obj['type']
        page = obj['page']
        size = obj['size']
    except KeyError:
        return JsonResponse({'status': 'key error'})

    if type not in TYPED_FOLDER:
        return JsonResponse({'status': 'wrong type'})

    typed_folder = TYPED_FOLDER[type]
    folders = typed_folder.objects.filter(folder__user=user)

    data = {
        'status': 'ok',
        'folders': [
            [
                str(f.folder.id),
                str(f.folder.user),
                str(f.folder.name),
                str(f.folder.about),
            ]
            for f in folders
        ],
    }

    return JsonResponse(data)
