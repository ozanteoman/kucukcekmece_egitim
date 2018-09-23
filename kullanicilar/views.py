from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user:
            login(request=request, user=user)
            msg = "Merhaba <b> %s </b> Sisteme Hoşgeldin" % (username)
            messages.success(request, message=msg, extra_tags='success')
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'kullanicilar/register.html', context={'form': form})
