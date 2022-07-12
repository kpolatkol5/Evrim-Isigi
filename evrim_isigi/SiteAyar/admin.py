from django.contrib import admin
from SiteAyar.models.footerKontrol import Footer_kontrol
from SiteAyar.models.genelGorunum import Site_gorunum
from SiteAyar.models.seo import Ana_sayfa_seo_ayar


admin.site.register(Site_gorunum)
admin.site.register(Ana_sayfa_seo_ayar)
admin.site.register(Footer_kontrol)
