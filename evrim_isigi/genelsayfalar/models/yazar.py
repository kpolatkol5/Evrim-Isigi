from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Yazar(models.Model): 

    yazar_adi           =   models.OneToOneField("auth.User", verbose_name="yazar adi", on_delete=models.CASCADE)
    isim                =   models.CharField(max_length=500 ,verbose_name="yazar adı ve soyadı" , default="kadir")
    yazar_pozisyonu     =   models.CharField(max_length=50 , null=True)
    instagram_adresi    =   models.URLField(max_length=500 , null=True , blank=True)
    facebook_adresi     =   models.URLField(max_length=500 , null=True , blank=True)
    youtube_adresi      =   models.URLField(max_length=500 , null=True , blank=True)
    twitter_adresi      =   models.URLField(max_length=500 , null=True , blank=True)
    web_site            =   models.URLField(max_length=500 , null=True , blank=True)
    yazar_aciklama      =   RichTextField(blank=True)
    yazar_resim         =   models.ImageField(upload_to="genelsayfalar" )
    yazar_resim_seo     =   models.CharField(max_length=70, default=True)


    def __str__(self):
        return self.isim


    class Meta: 
        verbose_name_plural = "Yazarlar Hakkında"