from django import forms
from .models import Album


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_isim', 'sanatci_isim', 'album_logo', 'album_tur', 'is_favorite']

    def __init__(self, *args, **kwargs):
        super(AlbumCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'is_favorite':
                self.fields[field].widget.attrs = {'class': 'form-control'}


class AlbumUpdateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_isim', 'sanatci_isim', 'album_logo', 'album_tur', 'is_favorite']

    def __init__(self, *args, **kwargs):
        super(AlbumUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'is_favorite':
                self.fields[field].widget.attrs = {'class': 'form-control'}
