# Generated by Django 3.2.8 on 2022-02-23 13:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genelsayfalar', '0007_catagories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='genelsayfalar'),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
