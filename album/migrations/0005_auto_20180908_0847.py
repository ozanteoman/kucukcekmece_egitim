# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-08 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_auto_20180901_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sarki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarki_isim', models.CharField(max_length=50, null=True, verbose_name='Şarkı İsim')),
                ('ses_dosyasi', models.FileField(null=True, upload_to='music', verbose_name='Ses Dosyası')),
            ],
            options={
                'verbose_name_plural': 'Şarkılar',
            },
        ),
        migrations.AlterField(
            model_name='album',
            name='album_isim',
            field=models.CharField(help_text='Albüm İsimi Giriniz', max_length=100, verbose_name='Albüm İsim'),
        ),
        migrations.AddField(
            model_name='sarki',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.Album'),
        ),
    ]
