from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from ..models import Stream, Streamer, Invite


@login_required(login_url='login')
def invite(request, link):
    inv = Invite.objects.filter(link=link).first()

    if not inv:
        return render(request, 'app_messages/invite_404.html')

    stream = inv.stream
    user = request.user

    is_member = Streamer.objects.filter(stream=stream, user=user).first()

    if is_member:
        id = stream.id
        return redirect('stream', id=id)

    context = {
        'link': link,
        'name': stream.name,
        'owner': stream.owner,
        'about': stream.about,
    }

    return render(request, 'app_messages/invite.html', context)
