from django import forms
from .models import Album, Sarki


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


class SongAddForm(forms.ModelForm):
    class Meta:
        model = Sarki
        fields = ['sarki_isim', 'ses_dosyasi', 'is_favorite']

    def __init__(self, *args, **kwargs):
        super(SongAddForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'is_favorite':
                self.fields[field].widget.attrs = {'class': 'form-control'}
        if self.instance:
            self.fields['ses_dosyasi'].required=False

    def clean_ses_dosyasi(self):
        value = self.cleaned_data.get('ses_dosyasi')

        extension = value.name.split('.')[-1]
        if extension != 'mp3':
            raise forms.ValidationError('Lütfen sadece mp3 uzantılı ses dosyası yükleyin')
        return value


class SongQueryForm(forms.Form):
    FAVORITE_OR_ALL = (
        ('all', 'Tüm Şarkılar'),
        ('favorites', 'Favori Şarkılar')
    )

    query = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=FAVORITE_OR_ALL,
                              required=False, initial='all')
