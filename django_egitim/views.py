from django.shortcuts import render, Http404, reverse, HttpResponseRedirect
from .forms import KullaniciForm

from album.models import Album, Sarki
from django.db.models import Q

sehirler_sozluk = {
    'adana': 'Adana sıcak bir şehirimiz',
    'istanbul': 'En yüksek nüfusa sahip şehirimiz',
    'konya': 'En yüksek yüz ölçümüne sahip şehrimiz'
}


def index(request):
    album_list = Album.objects.all()
    q = request.GET.get('q', None)
    if q:
        album_list = album_list.filter(
            Q(album_isim__icontains=q) | Q(sanatci_isim__icontains=q) | Q(album_tur__icontains=q))
        songs_list = Sarki.objects.filter(
            Q(sarki_isim__icontains=q) | Q(album__album_isim__icontains=q) | Q(album__album_tur__icontains=q) | Q(
                album__sanatci_isim__icontains=q))
        return render(request, 'index2.html', context={
            'album_list': album_list, 'songs_list': songs_list
        })

    return render(request, 'index2.html', context={'album_list': album_list})


def sehir(request, sehir):
    if sehir in sehirler_sozluk:
        info = sehirler_sozluk[sehir]
        context = {'sehir': sehir, 'info': info}
        return render(request, 'sehir.html', context=context)
    else:
        raise Http404


def sehir_delete(request, sehir):
    if not sehir in sehirler_sozluk:
        raise Http404

    url = reverse('index')
    sehirler_sozluk.pop(sehir)
    return HttpResponseRedirect(reverse('index'))


def form_calisma(request):
    print(request.GET)
    isim = request.GET.get('isim', None)
    soyisim = request.GET.get('soyisim', None)
    return render(request, 'form_calisma.html', context={
        'isim': isim,
        'soyisim': soyisim
    })


def form_calisma_yeni_yontem(request):
    request.GET.get('isim')
    form = KullaniciForm(data=request.GET)
    if form.is_valid():
        isim = form.cleaned_data.get('isim')
        soyisim = form.cleaned_data.get('soyisim')
        yas = form.cleaned_data.get('yas')
        mahalle = form.cleaned_data.get('mahalle')

        return render(request, 'form_calisa_new.html', context={
            'form': form, 'isim': isim, 'soyisim': soyisim, 'yas': yas, 'mahalle': mahalle
        })

    return render(request, 'form_calisa_new.html', context={
        'form': form
    })


def form_calisma_yeni_post(request):
    form = KullaniciForm()
    if request.method == "POST":
        form = KullaniciForm(data=request.POST)
        if form.is_valid():
            isim = form.cleaned_data.get('isim')
            soyisim = form.cleaned_data.get('soyisim')
            yas = form.cleaned_data.get('yas')
            mahalle = form.cleaned_data.get('mahalle')
            return render(request, 'form_calisma_post.html', context={
                'form': form, 'isim': isim, 'soyisim': soyisim, 'yas': yas, 'mahalle': mahalle
            })
        else:
            return render(request, 'form_calisma_post.html', context={
                'form': form
            })
        # print(request.POST)
        # print("----------------")
        # print(request.GET)
        # print("bir post işlemi gerçekleşti")
        # isim = request.POST.get('isim')
        # soyisim = request.POST.get('soyisim')
        # mahalle = request.POST.get('mahalle')
        # yas = request.POST.get('yas')

    return render(request, 'form_calisma_post.html',
                  context={'form': form})
