# Generated by Django 3.2.8 on 2022-03-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteAyar', '0006_site_gorunum_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_gorunum',
            name='favicon',
            field=models.FileField(default=True, upload_to='SiteAyar/favicon'),
        ),
    ]
