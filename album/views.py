from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages
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
    form = AlbumCreateForm()
    if request.method == "POST":
        form = AlbumCreateForm(data=request.POST, files=request.FILES or None)
        if form.is_valid():
            album = form.save()
            messages.success(request,"Tebrikler! Albüm Oluşturuldu.",extra_tags='success')
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
        album.delete()
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
