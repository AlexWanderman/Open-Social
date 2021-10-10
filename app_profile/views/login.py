# СТРАНИЦА входа

from django.shortcuts import render


def login(request):
    return render(request, 'app_profile/login.html')
