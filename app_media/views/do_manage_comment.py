import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from ..models import Comment, Folder, FolderComment, File, FileComment


@login_required(login_url='login')
def do_create_comment(request):
    '''Создание комментария к папке/файлу.'''
    obj = json.loads(request.body)
    print(obj)

    user = request.user
    text = obj['text']
    type = obj['type']
    id = obj['id']

    comment = Comment.objects.create(
        user=user,
        text=text,
    )
    comment.save()

    if type == 'folder':
        folder = Folder.objects.filter(id=id).first()

        type_comment = FolderComment.objects.create(
            comment=comment,
            folder=folder,
        )
        type_comment.save()
    else:
        file = File.objects.filter(id=id).first()

        type_comment = FileComment.objects.create(
            comment=comment,
            file=file,
        )
        type_comment.save()

    data = {'result': 'ok', 'id': comment.id}

    return JsonResponse(data)


@login_required(login_url='login')
def do_edit_comment(request):
    '''Изменение комментария к папке/файлу.'''
    obj = json.loads(request.body)
    print(obj)

    user = request.user
    id = obj['id']
    text = obj['text']

    comment = Comment.objects.filter(id=id, user=user).first()

    if not comment:
        return JsonResponse({'error': 'comment not found'})

    comment.text = text
    comment.save()

    return JsonResponse({'result': 'ok'})


@login_required(login_url='login')
def do_delete_comment(request):
    '''Удаление комментария к папке/файлу.'''
    obj = json.loads(request.body)
    print(obj)

    user = request.user
    id = obj['id']

    comment = Comment.objects.filter(id=id, user=user).first()

    if not comment:
        return JsonResponse({'error': 'comment not found'})

    comment.delete()

    return JsonResponse({'result': 'ok'})


@login_required(login_url='login')
def do_get_comments(request):
    '''Просмотр комментариев.'''
    obj = json.loads(request.body)
    print(obj)

    id = obj['id']

    if obj['type'] == 'folder':
        comments = FolderComment.objects.filter(folder__id=id)
    else:
        comments = FileComment.objects.filter(file__id=id)

    data = {
        'result': 'ok',
        'files': [
            [
                str(f.comment.id),
                str(f.comment.user),
                str(f.comment.text),
                str(f.comment.datetime)
            ]
            for f in comments
        ],
    }

    return JsonResponse(data)
