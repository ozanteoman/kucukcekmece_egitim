from django.conf.urls import url
from .views import album_create, album_detail, album_list, album_update, album_delete

urlpatterns = [
    url(r'^album-list/$', view=album_list, name='album-list'),
    url(r'^album-ekle/$', view=album_create, name='album-create'),
    url(r'^album-detail/(?P<slug>[\w-]+)/$', album_detail, name='album-detail'),
    url(r'^album-update/(?P<slug>[\w-]+)/$', album_update, name='album-update'),
    url(r'^album-delete/(?P<slug>[\w-]+)/$', album_delete, name='album-delete'),
]
