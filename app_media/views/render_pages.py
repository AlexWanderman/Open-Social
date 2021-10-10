from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def images(request):
    return render(request, 'app_media/images.html')


@login_required(login_url='login')
def videos(request):
    return render(request, 'app_media/videos.html')


@login_required(login_url='login')
def music(request):
    return render(request, 'app_media/music.html')


@login_required(login_url='login')
def podcasts(request):
    return render(request, 'app_media/podcasts.html')


@login_required(login_url='login')
def documents(request):
    return render(request, 'app_media/documents.html')
