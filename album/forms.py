from django import forms
from .models import Album


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_isim', 'sanatci_isim', 'album_tur', 'is_favorite']


class AlbumUpdateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_isim', 'sanatci_isim', 'album_tur', 'is_favorite']
