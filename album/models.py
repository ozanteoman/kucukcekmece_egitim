from django.db import models


class Album(models.Model):
    album_isim = models.CharField(max_length=100, verbose_name='Albüm İsim')
    sanatci_isim = models.CharField(max_length=100, verbose_name='Sanatçı İsim')
    album_tur = models.CharField(max_length=100, verbose_name='Albüm Tür')
    created_date = models.DateField(auto_now_add=True, auto_now=False, verbose_name='Albüm Çıkış Tarihi')
    is_favorite = models.BooleanField(default=False, verbose_name='Favorilerine Ekle')
    album_logo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return "%s-%s"%(self.album_isim,self.sanatci_isim)
