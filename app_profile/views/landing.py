from django.shortcuts import render, redirect


def landing(request):
    if request.user.is_authenticated:
        return redirect('profile')

    return render(request, 'app_profile/landing.html')
