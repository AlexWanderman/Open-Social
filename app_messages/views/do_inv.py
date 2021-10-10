import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from ..models import Stream, Streamer, Invite


@login_required(login_url='login')
def do_inv(request):
    obj = json.loads(request.body)
    print(obj)

    if 'link' not in obj:
        return JsonResponse({'result': 'error'})

    link = obj['link']
    invite = Invite.objects.filter(link=link).first()

    if not invite:
        return JsonResponse({'result': 'error'})

    stream = invite.stream
    user = request.user

    is_member = Streamer.objects.filter(stream=stream, user=user).first()

    if is_member:
        return JsonResponse({'result': 'is_member'})

    streamer = Streamer.objects.create(
        stream=stream,
        user=user,
        can_write=True,
    )
    streamer.save()

    return JsonResponse({'result': 'ok'})
