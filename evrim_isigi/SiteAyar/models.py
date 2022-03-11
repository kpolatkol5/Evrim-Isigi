from django.db import models
from django.utils.safestring import mark_safe
from genelsayfalar.models import *


# Create your models here.


class Site_gorunum(models.Model):
    logo=models.FileField(upload_to="SiteAyar/site_gorunum")
    is_active=models.BooleanField(default=False)
    logo_yazi=models.CharField(max_length=50 , verbose_name="logo yazisi")
    favicon=models.FileField(upload_to="SiteAyar/favicon", default=True)
    
    def __str__(self):
        return mark_safe(self.logo_yazi)


    class Meta:
        verbose_name_plural = "Site Görünüm "

class Ana_sayfa_seo_ayar(models.Model):
    is_active=models.BooleanField(default=True)
    meta_description=models.CharField(max_length=160 ,help_text="max 160 karekter uzunluğunda olmalıdır", verbose_name="description")
    meta_keywords=models.CharField(max_length=100 , db_index=True ,help_text="aralarına virgül konulacak şekilde max 5 anahtar kelime giriniz", verbose_name="meta keywords")
    meta_title=models.CharField(max_length=150, db_index=True ,)

    def __str__(self):
        return self.meta_title
    
    class Meta:
        verbose_name_plural = "Ana Sayfa Seo Ayar "

class Footer_kontrol(models.Model):
    footer_header=models.CharField(max_length=50 , default=True, )
    footer_text=RichTextField()
    footer_link_text=models.CharField(max_length=20, default=True)
    footer_link=models.URLField()
    alt_bilgi=models.CharField(max_length=150, blank=True ,default=False, verbose_name="alt açıklama")
    facebook=models.URLField()
    twitter=models.URLField()
    instagram=models.URLField()
    youtube=models.URLField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.footer_header

    class Meta:
        verbose_name_plural = "Footer Kontrol "





