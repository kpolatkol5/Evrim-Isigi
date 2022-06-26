from django.db import models
from genelsayfalar.models.kategoriler import Catagories


class Youtube(models.Model):
    title           =   models.CharField(max_length=200 ,verbose_name="Başlık")
    image           =   models.ImageField(upload_to="genelsayfalar/youtube" ,verbose_name="Resim")
    is_active       =   models.BooleanField(default=False , verbose_name="Aktif İçerik")
    date            =   models.DateField(verbose_name="Yüklenme Zamanı")
    url             =   models.URLField( verbose_name="Videonun Linki")
    kategori        =   models.ForeignKey(Catagories, on_delete=models.CASCADE)


    class Meta: 
        verbose_name_plural = "Youtube Ekle"


    def __str__(self):
        return self.title