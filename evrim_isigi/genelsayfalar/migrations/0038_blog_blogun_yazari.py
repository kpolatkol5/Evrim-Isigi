# Generated by Django 3.2.8 on 2022-02-28 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genelsayfalar', '0037_remove_blog_blogun_yazari'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogun_yazari',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='genelsayfalar.yazar'),
            preserve_default=False,
        ),
    ]