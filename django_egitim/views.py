from django.shortcuts import render, Http404, reverse, HttpResponseRedirect
from .forms import KullaniciForm

sehirler_sozluk = {
    'adana': 'Adana sıcak bir şehirimiz',
    'istanbul': 'En yüksek nüfusa sahip şehirimiz',
    'konya': 'En yüksek yüz ölçümüne sahip şehrimiz'
}


def index(request):
    return render(request=request, template_name='index.html', context={
        "sehirler": sehirler_sozluk
    })


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
