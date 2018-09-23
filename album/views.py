from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import AlbumCreateForm, AlbumUpdateForm, SongAddForm, SongQueryForm, SongsQueryForm2
from .models import Album, Sarki


def album_list(request):
    albumler = Album.objects.all()
    context = {'albumler': albumler}
    return render(request, 'album/album_list.html', context=context)


def album_update(request, slug):
    # album=Album.objects.get(pk=pk)
    album = get_object_or_404(Album, slug=slug)
    form = AlbumUpdateForm(instance=album)
    if request.method == "POST":
        form = AlbumUpdateForm(instance=album, data=request.POST, files=request.FILES or None)
        if form.is_valid():
            form.save()
            msg = "Tebrikler! %s isimli albüm başarıyla güncelledi." % (form.instance.album_isim)
            messages.success(request, msg, extra_tags='info')
            return HttpResponseRedirect(reverse('album-detail', kwargs={'slug': form.instance.slug}))
    context = {'form': form, 'album': album}
    return render(request, 'album/album_update.html', context=context)


def album_create(request):
    form = AlbumCreateForm()
    if request.method == "POST":
        form = AlbumCreateForm(data=request.POST, files=request.FILES or None)
        if form.is_valid():
            album = form.save()
            messages.success(request, "Tebrikler! Albüm Oluşturuldu.", extra_tags='success')
            return HttpResponseRedirect(reverse('album-detail', kwargs={'slug': album.slug}))
    context = {'form': form}
    return render(request, 'album/album_create.html', context=context)


def album_detail(request, slug):
    form = SongQueryForm(request.GET or None)
    page = request.GET.get('page', 1)
    try:
        album = Album.objects.get(slug=slug)
        songs = album.sarki_set.all()
        if form.is_valid():
            q = form.cleaned_data.get('query')
            if q == 'all':
                songs = album.sarki_set.all()
            elif q == 'favorites':
                songs = album.sarki_set.filter(is_favorite=True)

        paginator = Paginator(songs, 5)
        try:
            songs = paginator.page(page)
        except EmptyPage:
            songs = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            songs = paginator.page(1)

    except Album.DoesNotExist:
        return render(request, 'Http404.html')
    context = {'album': album, 'form': form, 'songs': songs}
    return render(request, 'album/album_detail.html', context=context)


def album_delete(request, slug):
    # album = get_object_or_404(Album, pk=pk)
    try:
        album = Album.objects.get(slug=slug)
        album.delete()
        msg = "%s isimli albüm başarıyla silindi" % (album.album_isim)
        messages.success(request, msg, extra_tags='danger')
    except Album.DoesNotExist:
        return render(request, 'Http404.html')
    return HttpResponseRedirect(reverse('album-list'))


def album_favori(request):
    if request.method == "POST":
        slug = request.POST.get('slug')
        album = Album.objects.get(slug=slug)
        if album.is_favorite == True:
            album.is_favorite = False
            album.save()
        else:
            album.is_favorite = True
            album.save()
        return HttpResponseRedirect(reverse('album-list'))


def add_song(request, slug):
    form = SongAddForm(data=request.POST or None, files=request.FILES or None)
    album = Album.objects.get(slug=slug)
    if form.is_valid():
        song = form.save(commit=False)
        song.album = album
        song.save()
        messages.success(request, "Tebrikler Bir Şarkı Eklediniz", extra_tags='success')
        return HttpResponseRedirect(reverse('album-detail', kwargs={'slug': album.slug}))
    return render(request, 'album/songs/add_song.html', context={'album': album, 'form': form})


def delete_song(request, slug, pk):
    album = Album.objects.get(slug=slug)
    song = Sarki.objects.get(album=album, pk=pk)
    song.delete()
    msg = "Tebrikler <b>%s</b> isimli şarkı başarıyla silindi" % (song.sarki_isim)
    messages.success(request, msg, extra_tags='danger')
    return HttpResponseRedirect(reverse('album-detail', kwargs={'slug': album.slug}))


def song_favorite(request, slug, pk):
    next = request.GET.get('next', reverse('album-detail', kwargs={'slug': slug}))
    album = Album.objects.get(slug=slug)
    # album.sarki_set.all() bu albüme ait olan tüm şarkılar getir.
    song = album.sarki_set.get(pk=pk)
    if song.is_favorite:
        song.is_favorite = False
    else:
        song.is_favorite = True
    song.save()
    return HttpResponseRedirect(next)  # geldiğin sayfaya geri git.


def song_update(request, slug, pk):
    album = Album.objects.get(slug=slug)
    song = album.sarki_set.get(pk=pk)
    form = SongAddForm(instance=song, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, 'Tebrikler Şarkınız Başarıyla Güncellendi.', extra_tags='success')
        return HttpResponseRedirect(reverse('album-detail', kwargs={'slug': album.slug}))

    context = {'album': album, 'form': form}
    return render(request, 'album/songs/update_song.html', context=context)


def songs_list(request):
    form = SongsQueryForm2(data=request.GET or None)
    songs = Sarki.objects.all()
    if form.is_valid():
        favorite_or_all = form.cleaned_data.get('favorite_or_all', None)
        album = form.cleaned_data.get('album', None)
        if favorite_or_all and favorite_or_all == 'favorites':
            songs = songs.filter(is_favorite=True)
        if album:
            songs = songs.filter(album=album)
    return render(request, 'album/songs/songs_list.html', context={'form': form, 'songs': songs})

