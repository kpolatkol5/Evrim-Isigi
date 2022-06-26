from django.shortcuts import render
from SiteAyar.models.footerKontrol import Footer_kontrol 
from SiteAyar.models.genelGorunum import Site_gorunum
from genelsayfalar.models.kategoriler import Catagories
from genelsayfalar.models.blog import Blog


def blog_detay(request , slug):


    context={
        "site_ayar"         :   Site_gorunum.objects.get(is_active=True),
        "blog"              :   Blog.objects.get(slug=slug),
        "kategori"          :   Catagories.objects.filter(is_active=True),
        "kategori_slug"     :   Blog.objects.get(slug=slug),
        "nav_blogs"         :   Blog.objects.filter(is_active=True).order_by("-id"),
        "footer_kontrol"    :   Footer_kontrol.objects.get(is_active=True)
    }


    return render(request, "genelsayfalar/blog_detay/blog_detay.html" ,context)