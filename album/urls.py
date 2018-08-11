from django.conf.urls import url
from .views import album_create, album_detail

urlpatterns = [
    url(r'^album-create/$', view=album_create, name='album-create'),
    url(r'^album-detail/(?P<pk>[0-9]+)/$', album_detail, name='album-detail')
]
