from django.db import models
from django.template.defaultfilters import slugify


class Album(models.Model):
    album_isim = models.CharField(max_length=100, verbose_name='Albüm İsim', help_text='Albüm İsimi Giriniz')
    slug = models.SlugField(max_length=200, null=True, unique=True)
    sanatci_isim = models.CharField(max_length=100, verbose_name='Sanatçı İsim')
    album_tur = models.CharField(max_length=100, verbose_name='Albüm Tür')
    created_date = models.DateField(auto_now_add=True, auto_now=False, verbose_name='Albüm Çıkış Tarihi')
    is_favorite = models.BooleanField(default=False, verbose_name='Favorilerine Ekle')
    album_logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s-%s" % (self.album_isim, self.sanatci_isim)

    def get_unique_slug(self):
        album_isim = self.album_isim
        template_slug = slugify(album_isim.replace('ı', 'i'))
        new_slug = template_slug
        sayac = 0
        while Album.objects.filter(slug=new_slug).exists():
            sayac += 1
            new_slug = "%s-%s" % (template_slug, sayac)
        return new_slug

    def get_album_photo(self):
        if self.album_logo:
            return self.album_logo.url
        return None

    def save(self, *args, **kwargs):
        if self.id == None:
            self.slug = self.get_unique_slug()
        else:
            last_album = Album.objects.get(slug=self.slug)
            if last_album.album_isim != self.album_isim:
                self.slug = self.get_unique_slug()
        super(Album, self).save(*args, **kwargs)


class Sarki(models.Model):
    album = models.ForeignKey(Album, null=True)
    sarki_isim = models.CharField(max_length=50, blank=False, null=True, verbose_name='Şarkı İsim')
    is_favorite = models.BooleanField(default=False)
    ses_dosyasi = models.FileField(upload_to='music', null=True, blank=False, verbose_name='Ses Dosyası')

    class Meta:
        verbose_name_plural = 'Şarkılar'

    def __str__(self):
        return "%s %s" % (self.album.album_isim, self.sarki_isim)
