import json

from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse


@login_required(login_url='login')
def do_setup(request):
    obj = json.loads(request.body)
    print(obj)

    if 'action' not in obj:
        return JsonResponse({'error': 'missing action'})

    action = obj['action']

    if action == 'change_password':
        p = ('ps_1', 'ps_2', 'ps_3')

        if not all(x in obj for x in p):
            return JsonResponse({'error': f'missing parameters for "{action}"'})

        ps_1 = obj['ps_1']
        ps_2 = obj['ps_2']
        ps_3 = obj['ps_3']

        user = authenticate(request, username=request.user, password=ps_1)

        if not user:
            return JsonResponse({'error': 'wrong old password'})

        if ps_2 != ps_3:
            return JsonResponse({'error': 'new password is not confirmed'})

        user.set_password(ps_2)
        update_session_auth_hash(request, user)

        return JsonResponse({'result': 'ok'})

    return JsonResponse({'error': 'wrong action'})
