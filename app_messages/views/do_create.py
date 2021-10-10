import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from ..models import Stream, Streamer, Invite


@login_required(login_url='login')
def do_create(request):
    obj = json.loads(request.body)
    print(obj)

    li = ('type', 'name', 'about')

    if not all(x in li for x in obj):
        return JsonResponse({'error': 'missing parametr'})

    type = obj['type']
    user = request.user
    name = obj['name']
    about = obj['about']

    # Создать "поток" нужного типа
    stream = Stream.objects.create(
        type=type,
        owner=user,
        name=name,
        about=about,
    )
    stream.save()

    # Добавить создавшего пользователя в участники
    streamer = Streamer.objects.create(
        stream=stream,
        user=user,
        can_write=True,
    )
    streamer.save()

    # Создать пригласительную ссылку
    invite = Invite.objects.create(
        stream=stream,
        # ссылка генерируется автоматически
    )
    invite.save()

    return JsonResponse({'result': 'ok'})
