from django.db import models
from ckeditor.fields import RichTextField


class Kitap_onerileri(models.Model):
    title               =   models.CharField(max_length=200 , verbose_name="Kitabın İsmi")
    image               =   models.ImageField(upload_to="genelsayfalar/kitap_onerileri")
    is_active           =   models.BooleanField(verbose_name="Aktif İçerik")
    kitap_aciklama      =   RichTextField(verbose_name="Kitap Hakkında")
    date                =   models.DateField(verbose_name="Yüklenme Zamanı")
    slug                =   models.SlugField(null=False ,blank=True , unique=True, db_index=True , editable=False)


    def __str__(self):
        return self.title


    def save(self , *args , **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)


    class Meta: 
        verbose_name_plural = "Kitap Önerileri"
