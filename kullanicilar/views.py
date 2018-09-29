from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def user_register(request):
    form = RegisterForm(data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        # register işlemi buraya kadar
        # sırada register olan kullanıcıyı sisteme login etmede..
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            msg = "Merhaba %s sisteme hoşgeldin." % (username)
            messages.success(request, msg, extra_tags='success')
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'kullanicilar/register.html', context=context)


def user_login(request):
    form = LoginForm(data=request.POST or None, request=request)
    if form.is_valid():
        # formda bir eksiklik yoksa...
        username = form.cleaned_data.get('username')
        msg = 'Merhaba %s sisteme hoşgeldiniz' % (username)
        messages.success(request, msg, extra_tags='success')
        return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'kullanicilar/login.html', context)


def user_logout(request):
    msg = 'Tekrar Görüşmek Dileğiyle Hoşçakal %s' % (request.user.username)
    messages.success(request, msg, extra_tags='success')
    logout(request)
    return HttpResponseRedirect(reverse('user-login'))
