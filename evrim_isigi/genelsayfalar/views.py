from django.shortcuts import render
from genelsayfalar.models import Blog , Catagories

# Create your views here.

def ana_sayfa(request):
    context={
        "blogs":Blog.objects.filter(is_active=True,is_home=True),
        "kategori":Catagories.objects.filter(is_active=True),
        "nav_blogs":Blog.objects.filter(is_active=True),
        "manset":Blog.objects.get(manset=True)
    }
    return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)


def sozluk(request):

    context={
    
        "kategori":Catagories.objects.filter(is_active=True)

    }


    return render(request , "genelsayfalar/sozluk.html" , context)

def blog_detay(request , slug):

    context={
        "blog":Blog.objects.get(slug=slug),
        "kategori":Catagories.objects.filter(is_active=True),
        "kategori_slug":Blog.objects.get(slug=slug),
        "nav_blogs":Blog.objects.filter(is_active=True)

    }


    return render(request, "genelsayfalar/blog_detay/blog_detay.html" ,context)


def blogun_kategorisi(request , slug):
  
    context={
        "blog":Catagories.objects.get(slug=slug).blog_set.filter(is_active=True),
        "kategori":Catagories.objects.filter(is_active=True),
        "nav_blogs":Blog.objects.filter(is_active=True)

    }

    return render(request, "genelsayfalar/kategori_sayfalari/katagori_detay.html", context)