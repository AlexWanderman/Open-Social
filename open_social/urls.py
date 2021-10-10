from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

import app_profile.urls as profile_urls
import app_messages.urls as messages_urls
import app_media.urls as media_urls


def page_debug(request):
    return render(request, 'debug_page.html')


urlpatterns = [
    # favicon
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico')),

    # debug_page
    path('', page_debug, name='page_debug'),

    # app_profile
    path('usr/', include(profile_urls)),

    # app_messages
    path('msg/', include(messages_urls)),

    # app_media
    path('mda/', include(media_urls)),

    # admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
