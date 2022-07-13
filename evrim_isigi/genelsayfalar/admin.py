from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from .models import Blog,Catagories,Yazar,Youtube,Kitap_onerileri

class Blog_Admin(admin.ModelAdmin):
    list_display = ("resim","title" , "is_active" ,"blogun_kategorisi", "secilen_etiketler" )
    readonly_fields=("slug",)
    

    def secilen_etiketler(self, obj):
        html="<ul>"

        for category in obj.ana_sayfa_etiket.all():
            html += "<li> " +category.name + "</li> "
        
        html += "</ul>"

        return mark_safe(html) 

    def resim(self , obj):
        if obj.image:
            img =   f'<img src="{obj.image.url}" width="120px height="120px "></img>'
            return mark_safe(img)
        else:
            return mark_safe("<p>Resim Yok</p>")

class Katagori_Admin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields=("slug",)



admin.site.register(Blog , Blog_Admin)
admin.site.register(Catagories,Katagori_Admin)
admin.site.register(Yazar)
admin.site.register(Youtube)
admin.site.register(Kitap_onerileri)