# СТРАНИЦА профиля

from django.shortcuts import render


def profile(request):
    context = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'name': request.user.name,
        'about': request.user.about,
        'birthday': request.user.birthday,
        'is_you': True,
    }

    return render(request, 'app_profile/profile.html', context)
