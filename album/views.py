from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import AlbumCreateForm
from .models import Album


def album_create(request):
    form = AlbumCreateForm()
    if request.method == "POST":
        form = AlbumCreateForm(data=request.POST)
        if form.is_valid():
            album = form.save()
            return HttpResponseRedirect(reverse('album-detail', kwargs={'pk': album.pk}))
    context = {'form': form}
    return render(request, 'album/album_create.html', context=context)


def album_detail(request, pk):
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return render(request, 'Http404.html')
    context = {'album': album}
    return render(request, 'album/album_detail.html', context=context)
