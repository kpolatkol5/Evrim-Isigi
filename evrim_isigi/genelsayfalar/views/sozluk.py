from django.shortcuts import render
from genelsayfalar.models.kategoriler import Catagories
from SiteAyar.models.genelGorunum import Site_gorunum
from SiteAyar.models.footerKontrol import Footer_kontrol 


def sozluk(request):

    context =   {
        "site_ayar"         :   Site_gorunum.objects.get(is_active=True),
        "kategori"          :   Catagories.objects.filter(is_active=True),
        "footer_kontrol"    :   Footer_kontrol.objects.get(is_active=True)
    }


    return render(request , "genelsayfalar/sozluk.html" , context)
