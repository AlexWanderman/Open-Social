# СТРАНИЦА настроек

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required(login_url='login')
def settings(request):
    user = request.user

    context = {}

    return render(request, 'app_profile/settings.html', context)
