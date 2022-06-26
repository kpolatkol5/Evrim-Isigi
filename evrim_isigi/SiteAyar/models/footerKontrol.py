from django.db import models
from ckeditor.fields import RichTextField


class Footer_kontrol(models.Model):
    footer_header       =   models.CharField(max_length=50 , default=True, )
    footer_text         =   RichTextField()
    footer_link_text    =   models.CharField(max_length=20, default=True)
    footer_link         =   models.URLField()
    alt_bilgi           =   models.CharField(max_length=150, blank=True ,default=False, verbose_name="alt açıklama")
    facebook            =   models.URLField()
    twitter             =   models.URLField()
    instagram           =   models.URLField()
    youtube             =   models.URLField()
    is_active           =   models.BooleanField(default=True)


    def __str__(self):
        return self.footer_header


    class Meta:
        verbose_name_plural = "Footer Kontrol "





