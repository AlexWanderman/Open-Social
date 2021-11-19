import json

from django import forms
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponse

from ..models import File, ImageFile, VideoFile, MusicFile, PodcastFile, DocumentFile

TYPED_FILE = {
    'image': ImageFile,
    'video': VideoFile,
    'music': MusicFile,
    'podcast': PodcastFile,
    'document': DocumentFile,
}


def create_file(user, raw_file, name):
    file = File.objects.create(
        user=user,
        file=raw_file,
        name=name,
    )

    return file


@login_required(login_url='login')
def do_create_file(request):
    '''Загрузка файла.'''
    print(f'FILES = {request.FILES}')
    print(f'POST = {request.POST}')

    if 'file' not in request.FILES or 'data' not in request.POST:
        return HttpResponse('error - wrong parameters')

    user = request.user
    raw_file = request.FILES['file']
    data = json.loads(request.POST['data'])

    if 'type' not in data or 'name' not in data:
        return HttpResponse('error - wrong parameters')

    type = data['type']
    name = data['name']

    if type == 'image':
        params = ('about', )

        if not all(x in data for x in params):
            return HttpResponse('error - wrong parameters')

        file = create_file(user, raw_file, name)
        file.save()

        image = ImageFile.objects.create(
            file=file,
            about=data['about'],
        )
        image.save()

    elif type == 'video':
        params = ('about', )

        if not all(x in data for x in params):
            return HttpResponse('error - wrong parameters')

        file = create_file(user, raw_file, name)
        file.save()

        video = VideoFile.objects.create(
            file=file,
            about=data['about'],
        )
        video.save()

    elif type == 'music':
        params = ('artist', 'genre', 'lyrics')

        if not all(x in data for x in params):
            return HttpResponse('error - wrong parameters')

        file = create_file(user, raw_file, name)
        file.save()

        music = MusicFile.objects.create(
            file=file,
            artist=data['artist'],
            genre=data['genre'],
            lyrics=data['lyrics'],
        )
        music.save()

    elif type == 'podcast':
        params = ('creator', 'theme', 'about')

        if not all(x in data for x in params):
            return HttpResponse('error - wrong parameters')

        file = create_file(user, raw_file, name)
        file.save()

        podcast = PodcastFile.objects.create(
            file=file,
            creator=data['creator'],
            theme=data['theme'],
            about=data['about'],
        )
        podcast.save()

    elif type == 'document':
        params = ('program', 'about')

        if not all(x in data for x in params):
            return HttpResponse('error - wrong parameters')

        file = create_file(user, raw_file, name)
        file.save()

        document = DocumentFile.objects.create(
            file=file,
            program=data['program'],
            about=data['about'],
        )
        document.save()

    else:
        return HttpResponse('error - wrong type')

    return HttpResponse('ok')


@login_required(login_url='login')
def do_edit_file(request):
    '''Редактирование параметров файла.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_edit_file'})


@login_required(login_url='login')
def do_delete_file(request):
    '''Удаление файла.'''
    obj = json.loads(request.body)
    print(obj)

    return JsonResponse({'result': 'do_delete_file'})


@login_required(login_url='login')
def do_get_files(request):
    '''Получение списка файлов.'''
    obj = json.loads(request.body)
    print(obj)

    if 'type' not in obj or obj['type'] not in TYPED_FILE:
        return JsonResponse({'status': 'wrong type'})

    user = request.user
    folder = obj['folder'] or None
    type = TYPED_FILE[obj['type']]
    files = type.objects.filter(file__user=user, file__folder__id=folder)

    data = {
        'status': 'ok',
        'files': [
            [
                str(f.file.id),
                str(f.file.file.url),
                str(f.file.user),
                str(f.file.name),
            ]
            for f in files],
    }

    return JsonResponse(data)
