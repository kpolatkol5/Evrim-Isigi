# Generated by Django 3.2.8 on 2022-03-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteAyar', '0002_auto_20220309_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_gorunum',
            name='logo',
            field=models.FileField(upload_to='SiteAyar/site_gorunum'),
        ),
    ]