# Generated by Django 3.2.8 on 2022-03-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteAyar', '0011_footer_kontrol_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer_kontrol',
            name='footer_link_text',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
