from django.urls import path, re_path

from . import views as v

urlpatterns = [
    path('register', v.register, name='register'),
    path('do_reg',   v.do_reg,   name='do_reg'),

    path('login',    v.login,    name='login'),
    path('do_in',    v.do_in,    name='do_in'),
    path('do_out',   v.do_out,   name='do_out'),

    path('profile',  v.profile,  name='profile'),
    re_path(r'^profile/(?P<name>[a-zA-Z0-9]+)', v.profile_link, name='profile_link'),

    path('settings', v.settings, name='settings'),
    path('do_setup', v.do_setup, name='do_setup'),
]
