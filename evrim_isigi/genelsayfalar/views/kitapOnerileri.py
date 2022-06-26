from django.shortcuts import render
from genelsayfalar.models.kitapOnerileri import Kitap_onerileri
from genelsayfalar.models.kategoriler import Catagories
from SiteAyar.models.genelGorunum import Site_gorunum


def kitap_onerileri_detay(request,slug):


    context={
        "site_ayar"         :   Site_gorunum.objects.get(is_active=True),
        "kitap_onerileri"   :   Kitap_onerileri.objects.get(slug=slug),
        "kategori"          :   Catagories.objects.filter(is_active=True),
    }


    return render(request, "genelsayfalar/kitap_onerileri/kitap_onerileri_detay.html" , context)