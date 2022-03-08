# Generated by Django 3.2.8 on 2022-03-05 08:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genelsayfalar', '0046_auto_20220303_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap_onerileri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Kitabın İsmi')),
                ('image', models.ImageField(upload_to='genelsayfalar/kitap_onerileri')),
                ('is_active', models.BooleanField(verbose_name='Aktif İçerik')),
                ('kitap_aciklama', ckeditor.fields.RichTextField(verbose_name='Kitap Hakkında')),
                ('date', models.DateField(verbose_name='Yüklenme Zamanı')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]
