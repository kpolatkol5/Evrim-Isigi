from django.shortcuts import render
from genelsayfalar.models import Blog , Catagories,Youtube,Kitap_onerileri
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
# Create your views here.

def ana_sayfa(request):

# genel bloglar başladı

    blog_list = Blog.objects.filter(is_active=True, is_home=True)[::-1]

    paginator = Paginator(blog_list,5) 

    page = request.GET.get('page')

    try:
        blogs=paginator.page(page)
    
    except PageNotAnInteger:
        blogs=paginator.page(1)
    
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)

# genel bloglar bitti

# bilim dunyası başladı

    bilim_dunyasi = Catagories.objects.get(name="Bilim").blog_set.filter(is_active=True)[::-1]

    paginator = Paginator(bilim_dunyasi,4) 

    page = request.GET.get('page')

    try:
        bilim_dunyasi_blog=paginator.page(page)

    except PageNotAnInteger:
        bilim_dunyasi_blog=paginator.page(1)

    except EmptyPage:
        bilim_dunyasi_blog=paginator.page(paginator.num_pages)

# bilim dunyası bitti

# biyoloji başladı

    biyoloji = Catagories.objects.get(name="Biyoloji").blog_set.filter(is_active=True)[::-1]
    
    paginator = Paginator(biyoloji,5) 

    page = request.GET.get('page')

    try:
        biyoloji_blog=paginator.page(page)
    
    except PageNotAnInteger:
        biyoloji_blog=paginator.page(1)
    
    except EmptyPage:
        biyoloji_blog=paginator.page(paginator.num_pages)

#biyoloji bitti   

# genetik başladı

    genetik = Catagories.objects.get(name="Genetik").blog_set.filter(is_active=True)[::-1]
    
    paginator = Paginator(genetik,6) 

    page = request.GET.get('page')

    try:
        genetik_blog=paginator.page(page)
    
    except PageNotAnInteger:
        genetik_blog=paginator.page(1)
    
    except EmptyPage:
        genetik_blog=paginator.page(paginator.num_pages)

#genetik bitti   

    context={
        "kitap_onerileri":Kitap_onerileri.objects.filter(is_active=True)[::-1],
        "biyoloji":biyoloji_blog,
        "blogs":blogs,
        "bilim_dunyasi":bilim_dunyasi_blog,
        "genetik_blog":genetik_blog,
        "kategori":Catagories.objects.filter(is_active=True),
        "nav_blogs":Blog.objects.filter(is_active=True)[::-1],
        "manset":Blog.objects.get(manset=True),
        "youtube":Youtube.objects.filter(is_active=True)[::-1]
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
        "nav_blogs":Blog.objects.filter(is_active=True)[::-1]

    }


    return render(request, "genelsayfalar/blog_detay/blog_detay.html" ,context)


def blogun_kategorisi(request , slug):
#pagination_basladi
    kategori_bloglari=Catagories.objects.get(slug=slug).blog_set.filter(is_active=True)[::-1]
   
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
        "blog":kategori_detay,
        "kategori":Catagories.objects.filter(is_active=True),
        "nav_blogs":Blog.objects.filter(is_active=True)[::-1]

    }

    return render(request, "genelsayfalar/kategori_sayfalari/katagori_detay.html", context)


def kitap_onerileri_detay(request,slug):
    context={
        "kitap_onerileri":Kitap_onerileri.objects.get(slug=slug),
        "kategori":Catagories.objects.filter(is_active=True),

    }

    return render(request, "genelsayfalar/kitap_onerileri/kitap_onerileri_detay.html" , context)
