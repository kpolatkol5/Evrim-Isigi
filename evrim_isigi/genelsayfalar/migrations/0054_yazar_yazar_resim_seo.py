# Generated by Django 3.2.8 on 2022-03-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genelsayfalar', '0053_auto_20220311_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='yazar',
            name='yazar_resim_seo',
            field=models.CharField(default=True, max_length=70),
        ),
    ]