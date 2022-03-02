from django.urls import path
from . import views 

urlpatterns = [
    path("" ,views.ana_sayfa , name="anasayfa"),
    path("sozluk" ,views.sozluk , name=" sozluk"),
    path("blog/<slug:slug>" , views.blog_detay , name="detay"),
    path("kategori/<slug:slug>" , views.blogun_kategorisi, name="kategori"),
   

]
