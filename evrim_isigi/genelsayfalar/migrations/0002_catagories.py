# Generated by Django 3.2.8 on 2022-02-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genelsayfalar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]