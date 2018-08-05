from django import forms


class KullaniciForm(forms.Form):
    isim = forms.CharField(max_length=100, help_text='Kullanici İsimi Girin')
    soyisim = forms.CharField(max_length=100)
    yas = forms.IntegerField(min_value=10, max_value=100)
    mahalle = forms.CharField(max_length=1000, widget=forms.Textarea)

    def clean(self):
        cleaned_data = self.cleaned_data
        isim = cleaned_data.get('isim')
        soyisim = cleaned_data.get('soyisim')
        if isim != 'mehmet' and soyisim != 'dayanan':
            self.add_error('soyisim', "Lütfen mehmet dayanan isim ve soyisimli kişi.")
            self.add_error('isim', "Lütfen mehmet dayanan isim ve soyisimli kişi.")
            raise forms.ValidationError('Lütfen mehmet dayanan isim ve soyisimli kişi.')
        return cleaned_data

    def clean_isim(self):
        isim = self.cleaned_data.get('isim')
        # if isim != 'mehmet':
        #     raise forms.ValidationError('Lütfen mehmet isimli kullanıcı bilgisini giriniz')
        # isim = isim.upper()
        return isim

    def clean_soyisim(self):
        soyisim = self.cleaned_data.get('soyisim')
        soyisim = soyisim.upper()
        return soyisim

    def clean_yas(self):
        yas = self.cleaned_data.get('yas')
        if yas < 18:
            raise forms.ValidationError('Yaş kriteriniz sağlanmadı')
        return yas

    def clean_mahalle(self):
        mahalle = self.cleaned_data.get('mahalle')
        return mahalle
