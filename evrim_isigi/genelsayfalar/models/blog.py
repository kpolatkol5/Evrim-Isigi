from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from genelsayfalar.models.yazar import Yazar
from genelsayfalar.models.kategoriler import Catagories


class Blog(models.Model):
    blogun_yazari       =   models.ForeignKey(Yazar, on_delete=models.CASCADE)
    title               =   models.CharField(max_length=200 ,verbose_name="Başlık")
    description         =   RichTextField( verbose_name="Blog İçeriği")
    image               =   models.ImageField(upload_to="genelsayfalar", blank=True , default="genelsayfalar/django3.png" ,  verbose_name="Blogun Fotoğrafı")
    image_seo           =   models.CharField(max_length=70, default=True)
    is_active           =   models.BooleanField(default=False , verbose_name="Aktif Blog")
    is_home             =   models.BooleanField(default=False, verbose_name="Ana Sayfada Göster")
    manset              =   models.BooleanField(default=False ,verbose_name="Manşet Alanında  Göster",  help_text="ÖNCE AKTİF OLAN MANSET BLOGUNU İNAKTİF HALE GETİRİN")
    ana_sayfa_etiket    =   models.ManyToManyField(Catagories ,verbose_name="Ana Sayfa Etiket" ,blank=True, related_name="etiketBlog")
    blogun_kategorisi   =   models.ForeignKey(Catagories ,verbose_name="Kategoriler",default=1,on_delete=models.CASCADE, related_name="blog")
    yayimlanma_tarihi   =   models.DateTimeField()
    yayimlanma_tarihi   =   models.DateTimeField()
    begeni              =   models.PositiveIntegerField(default=0)
    
    meta_description    =   models.CharField(max_length=160 ,default=False ,help_text="max 160 karekter uzunluğunda olmalıdır", verbose_name="Meta Description")
    meta_keywords       =   models.CharField(max_length=100 ,default=False, db_index=True ,help_text="aralarına virgül konulacak şekilde max 5 anahtar kelime giriniz", verbose_name="Anahtar Kelimeler")
    meta_title          =   models.CharField(max_length=150,default=False, db_index=True ,
    help_text="Buraya yazılan alan sayfa başlığıdır arama motorlarında görünecektir başlık kısmını da ekleyebilirsiniz max=150 karakter ve  sonuna  '|Site Adı ' eklemeyi unutmayın... ",
    verbose_name="Meta Title")
    slug                =   models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
    kaynakca            =   RichTextField(verbose_name="Kaynakça")


    def save(self , *args , **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title


    class Meta: 
        verbose_name_plural = "Makale Ekle"