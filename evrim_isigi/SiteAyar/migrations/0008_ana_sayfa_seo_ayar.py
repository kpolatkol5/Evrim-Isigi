# Generated by Django 3.2.8 on 2022-03-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteAyar', '0007_site_gorunum_favicon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ana_sayfa_seo_ayar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('meta_description', models.CharField(help_text='max 160 karekter uzunluğunda olmalıdır', max_length=160, verbose_name='description')),
                ('meta_keywords', models.CharField(db_index=True, help_text='aralarına virgül konulacak şekilde max 5 anahtar kelime giriniz', max_length=100, verbose_name='meta keywords')),
                ('meta_title', models.CharField(db_index=True, max_length=150)),
            ],
        ),
    ]
