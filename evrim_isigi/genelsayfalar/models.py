from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Yazar(models.Model): 

    yazar_adi=models.OneToOneField("auth.User", verbose_name="yazar adi", on_delete=models.CASCADE)
    isim=models.CharField(max_length=500 ,verbose_name="yazar adı ve soyadı" , default="kadir")
    yazar_pozisyonu=models.CharField(max_length=50 , null=True)
    instagram_adresi=models.URLField(max_length=500 , null=True , blank=True)
    facebook_adresi=models.URLField(max_length=500 , null=True , blank=True)
    youtube_adresi=models.URLField(max_length=500 , null=True , blank=True)
    twitter_adresi=models.URLField(max_length=500 , null=True , blank=True)
    web_site=models.URLField(max_length=500 , null=True , blank=True)
    yazar_aciklama=RichTextField(blank=True)
    yazar_resim = models.ImageField(upload_to="genelsayfalar" )

    def __str__(self):
        return self.isim
    

class Catagories(models.Model):
    name = models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    slug  = models.SlugField(null=False ,blank=True , unique=True, db_index=True , editable=False)

    def save(self , *args , **kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
            
    def __str__(self):
        return self.name


class Blog(models.Model):
    blogun_yazari=models.ForeignKey(Yazar, on_delete=models.CASCADE)
    title= models.CharField(max_length=200 ,verbose_name="Başlık")
    description = RichTextField( verbose_name="Blog İçeriği")
    image = models.ImageField(upload_to="genelsayfalar", verbose_name="Blogun Fotoğrafı")
    is_active=models.BooleanField(default=False , verbose_name="Aktif Blog")
    is_home = models.BooleanField(default=False, verbose_name="Ana Sayfada Göster")
    manset=models.BooleanField(default=False,verbose_name="Manşet Alanında  Göster")
    blogun_kategorisi=models.ManyToManyField(Catagories ,verbose_name="Kategoriler")
    yayimlanma_tarihi = models.DateTimeField()
    slug  = models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
    kaynakca=RichTextField(verbose_name="Kaynakça")

    def save(self , *args , **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title


class Youtube(models.Model):
    title=models.CharField(max_length=200 ,verbose_name="Başlık")
    image = models.ImageField(upload_to="genelsayfalar/youtube" ,verbose_name="Resim")
    is_active=models.BooleanField(default=False , verbose_name="Aktif İçerik")
    date=models.DateField(verbose_name="Yüklenme Zamanı")
    url=models.URLField( verbose_name="Videonun Linki")
    kategori=models.ForeignKey(Catagories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Kitap_onerileri(models.Model):
    title=models.CharField(max_length=200 , verbose_name="Kitabın İsmi")
    image=models.ImageField(upload_to="genelsayfalar/kitap_onerileri")
    is_active = models.BooleanField(verbose_name="Aktif İçerik")
    kitap_aciklama=RichTextField(verbose_name="Kitap Hakkında")
    date=models.DateField(verbose_name="Yüklenme Zamanı")
    slug  = models.SlugField(null=False ,blank=True , unique=True, db_index=True , editable=False)

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
 



