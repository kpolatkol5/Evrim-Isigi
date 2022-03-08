from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from .models import Blog,Catagories,Yazar,Youtube,Kitap_onerileri

class Blog_Admin(admin.ModelAdmin):
    list_display = ("title" , "is_active" , "is_home" , "selected_categories")
    readonly_fields=("slug",)


    def selected_categories(self, obj):
        html="<ul>"

        for category in obj.blogun_kategorisi.all():
            html += "<li> " +category.name + "</li> "
        
        html += "</ul>"
    
        return mark_safe(html) 


class Katagori_Admin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields=("slug",)





admin.site.register(Blog , Blog_Admin)
admin.site.register(Catagories,Katagori_Admin)
admin.site.register(Yazar)
admin.site.register(Youtube)
admin.site.register(Kitap_onerileri)