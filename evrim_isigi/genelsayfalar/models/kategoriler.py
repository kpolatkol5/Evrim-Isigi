from django.db import models


class Catagories(models.Model):
    name                =   models.CharField(max_length=200, db_index=True ,)
    is_active           =   models.BooleanField(default=True, db_index=True ,)
    slug                =   models.SlugField(null=False ,blank=True , unique=True, db_index=True , editable=False)
    meta_description    =   models.CharField(max_length=160 ,help_text="max 160 karekter uzunluğunda olmalıdır", verbose_name="description")
    meta_keywords       =   models.CharField(max_length=100 , db_index=True ,help_text="aralarına virgül konulacak şekilde max 5 anahtar kelime giriniz", verbose_name="meta keywords")
    meta_title          =   models.CharField(max_length=150, db_index=True ,)


    def save(self , *args , **kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.name


    class Meta: 
        verbose_name_plural = "Katagoriler"
    
