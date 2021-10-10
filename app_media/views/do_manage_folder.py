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
    '''Создание папки.'''
    obj = json.loads(request.body)
    print(obj)

    if 'type' not in obj or obj['type'] not in TYPED_FOLDER:
        return JsonResponse({'error': 'wrong type'})

    user = request.user
    type = TYPED_FOLDER[obj['type']]

    folder = Folder.objects.create(
        user=user,
        name=obj['name'],
        about=obj['about'],
    )
    folder.save()

    image_folder = type.objects.create(
        folder=folder,
    )
    image_folder.save()

    return JsonResponse({'result': 'ok', 'id': folder.id})


@login_required(login_url='login')
def do_edit_folder(request):
    '''Редактирование папки.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_edit_folder'})


@login_required(login_url='login')
def do_delete_folder(request):
    '''Удаление папки.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_delete_folder'})


@login_required(login_url='login')
def do_get_folders(request):
    '''Получение списка папок.'''
    obj = json.loads(request.body)
    print(obj)

    if 'type' not in obj or obj['type'] not in TYPED_FOLDER:
        return JsonResponse({'error': 'wrong type'})

    user = request.user
    type = TYPED_FOLDER[obj['type']]
    folders = type.objects.filter(folder__user=user)

    data = {
        'result': 'ok',
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
