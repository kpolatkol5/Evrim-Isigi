from django.db import models


class Ana_sayfa_seo_ayar(models.Model):
    is_active           =   models.BooleanField(default=True)
    meta_description    =   models.CharField(max_length=160 ,help_text="max 160 karekter uzunluğunda olmalıdır", verbose_name="description")
    meta_keywords       =   models.CharField(max_length=100 , db_index=True ,help_text="aralarına virgül konulacak şekilde max 5 anahtar kelime giriniz", verbose_name="meta keywords")
    meta_title          =   models.CharField(max_length=150, db_index=True ,)


    def __str__(self):
        return self.meta_title


    class Meta:
        verbose_name_plural = "Ana Sayfa Seo Ayar "