# Generated by Django 3.2.8 on 2022-03-02 20:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genelsayfalar', '0043_auto_20220302_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='manset',
            field=models.BooleanField(default=False, verbose_name='Manşet Alanında  Göster'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogun_kategorisi',
            field=models.ManyToManyField(to='genelsayfalar.Catagories', verbose_name='Kategoriler'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Blog İçeriği'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='genelsayfalar', verbose_name='Blogun Fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Aktif Blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_home',
            field=models.BooleanField(default=False, verbose_name='Ana Sayfada Göster'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='kaynakca',
            field=ckeditor.fields.RichTextField(verbose_name='Kaynakça'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
    ]