from django.shortcuts import  render, Http404, reverse, HttpResponseRedirect

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
