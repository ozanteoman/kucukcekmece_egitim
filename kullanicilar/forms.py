from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(label='Parola Doğrulama',widget=forms.PasswordInput, required=True)
    password = forms.CharField(label='Parola',widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
