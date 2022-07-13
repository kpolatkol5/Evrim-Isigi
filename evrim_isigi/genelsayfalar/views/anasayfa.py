from django.shortcuts import render
from genelsayfalar.models.blog import Blog
from genelsayfalar.models.kitapOnerileri import Kitap_onerileri
from genelsayfalar.models.kategoriler import Catagories
from genelsayfalar.models.youtube import Youtube
from SiteAyar.models.genelGorunum import Site_gorunum
from SiteAyar.models.seo import Ana_sayfa_seo_ayar 
from SiteAyar.models.footerKontrol import Footer_kontrol 

def ana_sayfa(request):

    def kategori_blog(kategori):
        result  =   []

        for i in kategori:
            makaleler = Catagories.objects.get(name =   i.name).etiketBlog.filter(is_active="True")
            result.append({
                    "kategori_adi"  :   i.kategori_baslik ,
                    "makaleler"     :   makaleler.order_by("-id")[:5] , 
                    "nav_blog"      :   makaleler.order_by("-begeni")
                 })

        return result


    kitap_onerileri     =   Kitap_onerileri.objects.filter(is_active=True)
    kategori            =   Catagories.objects.filter(is_active=True)
    kategorideki_blog    =   kategori_blog(kategori)
    blogs               =   Blog.objects.filter(is_active=True, is_home=True).order_by("-id")[:5]
    nav_blogs           =   Blog.objects.filter(is_active=True).order_by("-id")
    youtube             =   Youtube.objects.filter(is_active=True).order_by("-id")
    site_ayar           =   Site_gorunum.objects.get(is_active=True)
    manset              =   Blog.objects.get(manset=True)
    ana_sayfa_seo       =   Ana_sayfa_seo_ayar.objects.get(is_active=True)
    footer_kontrol      =   Footer_kontrol.objects.get(is_active=True)


    context =   {
        "kitap_onerileri"   :   kitap_onerileri,
        "blogs"             :   blogs,
        "kategorideki_blog" :   kategorideki_blog,
        "kategori"          :   kategori,
        "nav_blogs"         :   nav_blogs,
        "manset"            :   manset ,
        "youtube"           :   youtube ,
        "site_ayar"         :   site_ayar,
        "ana_sayfa_seo"     :   ana_sayfa_seo,
        "footer_kontrol"    :   footer_kontrol 
    }


    return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)