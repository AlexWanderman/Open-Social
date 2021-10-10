import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from ..models import Stream, Streamer, Invite


@login_required(login_url='login')
def do_manage(request):
    obj = json.loads(request.body)
    print(obj)

    if 'action' not in obj or 'id' not in obj:
        return JsonResponse({'error': 'missing parametrs'})

    stream = Stream.objects.filter(id=obj['id']).first()
    action = obj['action']

    if action == 'create':
        invite = Invite.objects.create(stream=stream)
        invite.save()

        return JsonResponse({'result': 'ok'})

    if 'link' not in obj:
        return JsonResponse({'error': 'missing parametrs'})

    link = obj['link']
    invite = Invite.objects.filter(id=link).first()
    invite.delete()

    return JsonResponse({'result': 'ok'})
