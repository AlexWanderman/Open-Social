from django.urls import path, re_path


from . import views as v

urlpatterns = [
    path('images',    v.images,    name='images'),
    path('videos',    v.videos,    name='videos'),
    path('music',     v.music,     name='music'),
    path('podcasts',  v.podcasts,  name='podcasts'),
    path('documents', v.documents, name='documents'),

    path('do_create_folder', v.do_create_folder, name='do_create_folder'),
    path('do_edit_folder',   v.do_edit_folder,   name='do_edit_folder'),
    path('do_delete_folder', v.do_delete_folder, name='do_delete_folder'),
    path('do_get_folders',   v.do_get_folders,   name='do_get_folders'),

    path('do_create_file',   v.do_create_file,   name='do_create_file'),
    path('do_edit_file',     v.do_edit_file,     name='do_edit_file'),
    path('do_delete_file',   v.do_delete_file,   name='do_delete_file'),
    path('do_get_files',     v.do_get_files,     name='do_get_files'),

    path('do_create_saved',   v.do_create_saved,   name='do_create_saved'),
    path('do_delete_saved',   v.do_delete_saved,   name='do_delete_saved'),

    path('do_create_comment',   v.do_create_comment,   name='do_create_comment'),
    path('do_edit_comment',     v.do_edit_comment,     name='do_edit_comment'),
    path('do_delete_comment',   v.do_delete_comment,   name='do_delete_comment'),
    path('do_get_comments',     v.do_get_comments,     name='do_get_comments'),
]
