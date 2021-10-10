# СТРАНИЦА регистрации

from django.shortcuts import render


def register(request):
    return render(request, 'app_profile/register.html')
