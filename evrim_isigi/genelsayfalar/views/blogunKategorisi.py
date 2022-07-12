from django.shortcuts import render
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from genelsayfalar.models.kategoriler import Catagories
from genelsayfalar.models.blog import Blog
from SiteAyar.models.footerKontrol import Footer_kontrol
from SiteAyar.models.genelGorunum import Site_gorunum


def blogun_kategorisi(request , slug):

    #pagination_basladi

    kategori_bloglari   =   Catagories.objects.get(slug=slug).blog.filter(is_active=True).order_by("-id")
    paginator           =   Paginator(kategori_bloglari,15) 
    page                =   request.GET.get('page')


    try:
        kategori_detay=paginator.page(page)
    
    except PageNotAnInteger:
        kategori_detay=paginator.page(1)
    
    except EmptyPage:
        kategori_detay=paginator.page(paginator.num_pages)
    #pagination_bitti


    context={
        "site_ayar"             :   Site_gorunum.objects.get(is_active=True),
        "blog"                  :   kategori_detay,
        "kategori"              :   Catagories.objects.filter(is_active=True),
        "SeoAyar_kategoriler"   :   Catagories.objects.get(slug=slug),
        "nav_blogs"             :   Blog.objects.filter(is_active=True).order_by("-id"),
        "footer_kontrol"        :   Footer_kontrol.objects.get(is_active=True)

    }

    return render(request, "genelsayfalar/kategori_sayfalari/katagori_detay.html", context)
