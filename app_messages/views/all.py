'''Страница всех чатов пользователя.'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models import Streamer


@login_required(login_url='login')
def all(request):
    user = request.user
    chats = Streamer.objects.filter(user=user)

    context = {'chats': chats}

    return render(request, 'app_messages/all.html', context)
