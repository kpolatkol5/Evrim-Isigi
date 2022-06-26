from django.shortcuts import render
from genelsayfalar.models.blog import Blog
from genelsayfalar.models.kitapOnerileri import Kitap_onerileri
from genelsayfalar.models.kategoriler import Catagories
from genelsayfalar.models.youtube import Youtube
from SiteAyar.models.genelGorunum import Site_gorunum
from SiteAyar.models.seo import Ana_sayfa_seo_ayar 
from SiteAyar.models.footerKontrol import Footer_kontrol 






def ana_sayfa(request):


    kitap_onerileri     =   Kitap_onerileri.objects.filter(is_active=True)
    biyoloji            =   Catagories.objects.get(name="Biyoloji").blog_set.filter(is_active=True).order_by("-id")[:5]
    blogs               =   Blog.objects.filter(is_active=True, is_home=True).order_by("-id")[:5]
    bilim_dunyasi       =   Catagories.objects.get(name="Bilim").blog_set.filter(is_active=True).order_by("-id")[:4]
    genetik_blog        =   Catagories.objects.get(name="Genetik").blog_set.filter(is_active=True).order_by("-id")[:6]
    kategori            =   Catagories.objects.filter(is_active=True)
    nav_blogs           =   Blog.objects.filter(is_active=True).order_by("-id")
    manset              =   Blog.objects.get(manset=True)
    youtube             =   Youtube.objects.filter(is_active=True).order_by("-id")
    site_ayar           =   Site_gorunum.objects.get(is_active=True)
    ana_sayfa_seo       =   Ana_sayfa_seo_ayar.objects.get(is_active=True)
    footer_kontrol      =   Footer_kontrol.objects.get(is_active=True)


    context =   {
        "kitap_onerileri"   :   kitap_onerileri,
        "biyoloji"          :   biyoloji,
        "blogs"             :   blogs,
        "bilim_dunyasi"     :   bilim_dunyasi ,
        "genetik_blog"      :   genetik_blog ,
        "kategori"          :   kategori,
        "nav_blogs"         :   nav_blogs,
        "manset"            :   manset ,
        "youtube"           :   youtube ,
        "site_ayar"         :   site_ayar,
        "ana_sayfa_seo"     :   ana_sayfa_seo,
        "footer_kontrol"    :   footer_kontrol 
    }


    return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)