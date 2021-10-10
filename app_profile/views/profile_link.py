# Страница профиля по идентификатору

from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


def profile_link(request, name):
    user = User.objects.filter(name=name).first()

    if not user:
        return render(request, 'app_profile/profile_404.html', {'name': name})

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'name': user.name,
        'about': user.about,
        'birthday': user.birthday,
        'is_you': user == request.user,
    }

    return render(request, 'app_profile/profile.html', context)
