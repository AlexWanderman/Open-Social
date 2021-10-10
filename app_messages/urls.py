from django.urls import path, re_path

from . import views as v

urlpatterns = [
    path('all',       v.all,       name='all'),
    path('do_create', v.do_create, name='do_create'),
    re_path(r'^id=(?P<id>[a-zA-Z0-9_]+)',  v.stream,   name='stream'),
    re_path(r'^in=(?P<link>[a-zA-Z0-9_]+)', v.invite, name='invite'),
    path('do_inv',    v.do_inv,    name='do_inv'),
    path('da_manage', v.do_manage, name='do_manage'),
]
