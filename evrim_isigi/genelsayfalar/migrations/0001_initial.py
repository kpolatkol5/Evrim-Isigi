# Generated by Django 3.2.8 on 2022-07-11 06:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('meta_description', models.CharField(help_text='max 160 karekter uzunluğunda olmalıdır', max_length=160, verbose_name='description')),
                ('meta_keywords', models.CharField(db_index=True, help_text='aralarına virgül konulacak şekilde max 5 anahtar kelime giriniz', max_length=100, verbose_name='meta keywords')),
                ('meta_title', models.CharField(db_index=True, max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Katagoriler',
            },
        ),
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
            options={
                'verbose_name_plural': 'Kitap Önerileri',
            },
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('image', models.ImageField(upload_to='genelsayfalar/youtube', verbose_name='Resim')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif İçerik')),
                ('date', models.DateField(verbose_name='Yüklenme Zamanı')),
                ('url', models.URLField(verbose_name='Videonun Linki')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genelsayfalar.catagories')),
            ],
            options={
                'verbose_name_plural': 'Youtube Ekle',
            },
        ),
        migrations.CreateModel(
            name='Yazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='kadir', max_length=500, verbose_name='yazar adı ve soyadı')),
                ('yazar_pozisyonu', models.CharField(max_length=50, null=True)),
                ('instagram_adresi', models.URLField(blank=True, max_length=500, null=True)),
                ('facebook_adresi', models.URLField(blank=True, max_length=500, null=True)),
                ('youtube_adresi', models.URLField(blank=True, max_length=500, null=True)),
                ('twitter_adresi', models.URLField(blank=True, max_length=500, null=True)),
                ('web_site', models.URLField(blank=True, max_length=500, null=True)),
                ('yazar_aciklama', ckeditor.fields.RichTextField(blank=True)),
                ('yazar_resim', models.ImageField(upload_to='genelsayfalar')),
                ('yazar_resim_seo', models.CharField(default=True, max_length=70)),
                ('yazar_adi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='yazar adi')),
            ],
            options={
                'verbose_name_plural': 'Yazarlar Hakkında',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Blog İçeriği')),
                ('image', models.ImageField(blank=True, default='genelsayfalar/django3.png', upload_to='genelsayfalar', verbose_name='Blogun Fotoğrafı')),
                ('image_seo', models.CharField(default=True, max_length=70)),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif Blog')),
                ('is_home', models.BooleanField(default=False, verbose_name='Ana Sayfada Göster')),
                ('manset', models.BooleanField(default=False, help_text='ÖNCE AKTİF OLAN MANSET BLOGUNU İNAKTİF HALE GETİRİN', verbose_name='Manşet Alanında  Göster')),
                ('yayimlanma_tarihi', models.DateTimeField()),
                ('meta_description', models.CharField(default=False, help_text='max 160 karekter uzunluğunda olmalıdır', max_length=160, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(db_index=True, default=False, help_text='aralarına virgül konulacak şekilde max 5 anahtar kelime giriniz', max_length=100, verbose_name='Anahtar Kelimeler')),
                ('meta_title', models.CharField(db_index=True, default=False, help_text="Buraya yazılan alan sayfa başlığıdır arama motorlarında görünecektir başlık kısmını da ekleyebilirsiniz max=150 karakter ve  sonuna  '|Site Adı ' eklemeyi unutmayın... ", max_length=150, verbose_name='Meta Title')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('kaynakca', ckeditor.fields.RichTextField(verbose_name='Kaynakça')),
                ('blogun_kategorisi', models.ManyToManyField(to='genelsayfalar.Catagories', verbose_name='Kategoriler')),
                ('blogun_yazari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genelsayfalar.yazar')),
            ],
            options={
                'verbose_name_plural': 'Makale Ekle',
            },
        ),
    ]
