'''Страница конкретного чата.'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..models import Message, Streamer, Stream, Invite


@login_required(login_url='login')
def stream(request, id):
    # 1 Понять является ли user участником стрима с этим id
    user = request.user
    stream = Stream.objects.filter(id=id).first()
    is_member = Streamer.objects.filter(user=user, stream=stream)

    if not is_member:
        return render(request, 'app_messages/stream_404.html', {'id': id})

    # 2 Получить последние сообщения
    messages = Message.objects.filter(stream=stream)

    invites = Invite.objects.filter(stream=stream)

    context = {
        'id': id,
        'type': stream.type,
        'messages': messages,
        'invites': invites,
    }

    return render(request, 'app_messages/stream.html', context)
