from django.shortcuts import render
from genelsayfalar.models import Blog , Catagories,Youtube,Kitap_onerileri
from SiteAyar.models import *
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
# Create your views here.

def ana_sayfa(request):

    context={
        "kitap_onerileri":Kitap_onerileri.objects.filter(is_active=True).order_by("-id"),
        "biyoloji":Catagories.objects.get(name="Biyoloji").blog_set.filter(is_active=True).order_by("-id")[:5],
        "blogs":Blog.objects.filter(is_active=True, is_home=True).order_by("-id")[:5],
        "bilim_dunyasi": Catagories.objects.get(name="Bilim").blog_set.filter(is_active=True).order_by("-id")[:4],
        "genetik_blog":Catagories.objects.get(name="Genetik").blog_set.filter(is_active=True).order_by("-id")[:6],
        "kategori":Catagories.objects.filter(is_active=True),
        "nav_blogs":Blog.objects.filter(is_active=True).order_by("-id"),
        "manset":Blog.objects.get(manset=True),
        "youtube":Youtube.objects.filter(is_active=True).order_by("-id"),
        "site_ayar":Site_gorunum.objects.get(is_active=True),
        "ana_sayfa_seo":Ana_sayfa_seo_ayar.objects.get(is_active=True),
        "footer_kontrol":Footer_kontrol.objects.get(is_active=True)

    }
    return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)


def sozluk(request):

    context={
        "site_ayar":Site_gorunum.objects.get(is_active=True),
        "kategori":Catagories.objects.filter(is_active=True),
        "footer_kontrol":Footer_kontrol.objects.get(is_active=True)
    }


    return render(request , "genelsayfalar/sozluk.html" , context)

def blog_detay(request , slug):

    context={
        "site_ayar":Site_gorunum.objects.get(is_active=True),
        "blog":Blog.objects.get(slug=slug),
        "kategori":Catagories.objects.filter(is_active=True),
        "kategori_slug":Blog.objects.get(slug=slug),
        "nav_blogs":Blog.objects.filter(is_active=True).order_by("-id"),
        "footer_kontrol":Footer_kontrol.objects.get(is_active=True)
    }

    return render(request, "genelsayfalar/blog_detay/blog_detay.html" ,context)


def blogun_kategorisi(request , slug):
#pagination_basladi
    kategori_bloglari=Catagories.objects.get(slug=slug).blog_set.filter(is_active=True).order_by("-id")
   
    paginator = Paginator(kategori_bloglari,15) 

    page = request.GET.get('page')

    try:
        kategori_detay=paginator.page(page)
    
    except PageNotAnInteger:
        kategori_detay=paginator.page(1)
    
    except EmptyPage:
        kategori_detay=paginator.page(paginator.num_pages)
#pagination_bitti
    context={
        "site_ayar":Site_gorunum.objects.get(is_active=True),
        "blog":kategori_detay,
        "kategori":Catagories.objects.filter(is_active=True),
        "SeoAyar_kategoriler":Catagories.objects.get(slug=slug),
        "nav_blogs":Blog.objects.filter(is_active=True).order_by("-id"),
        "footer_kontrol":Footer_kontrol.objects.get(is_active=True)

    }

    return render(request, "genelsayfalar/kategori_sayfalari/katagori_detay.html", context)


def kitap_onerileri_detay(request,slug):
    context={
        "site_ayar":Site_gorunum.objects.get(is_active=True),
        "kitap_onerileri":Kitap_onerileri.objects.get(slug=slug),
        "kategori":Catagories.objects.filter(is_active=True),

    }

    return render(request, "genelsayfalar/kitap_onerileri/kitap_onerileri_detay.html" , context)
