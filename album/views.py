from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .forms import AlbumCreateForm, AlbumUpdateForm
from .models import Album


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
            return HttpResponseRedirect(reverse('album-detail', kwargs={'slug': form.instance.slug}))
    context = {'form': form}
    return render(request, 'album/album_update.html', context=context)


def album_create(request):
    print(request.FILES)
    form = AlbumCreateForm()
    if request.method == "POST":
        form = AlbumCreateForm(data=request.POST, files=request.FILES or None)
        if form.is_valid():
            album = form.save()
            return HttpResponseRedirect(reverse('album-detail', kwargs={'slug': album.slug}))
    context = {'form': form}
    return render(request, 'album/album_create.html', context=context)


def album_detail(request, slug):
    try:
        album = Album.objects.get(slug=slug)
    except Album.DoesNotExist:
        return render(request, 'Http404.html')
    context = {'album': album}
    return render(request, 'album/album_detail.html', context=context)


def album_delete(request, slug):
    # album = get_object_or_404(Album, pk=pk)
    try:
        album = Album.objects.get(slug=slug)
    except Album.DoesNotExist:
        return render(request, 'Http404.html')
    if request.method == "POST":
        album.delete()
        #  album_pk = request.POST.get('album_sil', None)
        #  print(al)
        #  silinecek_album = get_object_or_404(Album, pk=album_pk)
        #  silinecek_album.delete()
        return HttpResponseRedirect(reverse('album-list'))

    # album.delete()
    return render(request=request, template_name='album/album_delete.html', context={'album': album})
