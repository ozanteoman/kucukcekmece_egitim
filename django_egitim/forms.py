from django import forms


class KullaniciForm(forms.Form):
    isim = forms.CharField(max_length=100,help_text='Kullanici İsimi Girin')
    soyisim = forms.CharField(max_length=100)
    yas = forms.IntegerField(min_value=10,max_value=100)
    mahalle =forms.CharField(max_length=1000,widget=forms.Textarea)
