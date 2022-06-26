from django.db import models
from django.utils.safestring import mark_safe


class Site_gorunum(models.Model):
    logo        =   models.FileField(upload_to="SiteAyar/site_gorunum")
    is_active   =   models.BooleanField(default=False)
    logo_yazi   =   models.CharField(max_length=50 , verbose_name="logo yazisi")
    favicon     =   models.FileField(upload_to="SiteAyar/favicon", default=True)


    def __str__(self):
        return mark_safe(self.logo_yazi)


    class Meta:
        verbose_name_plural = "Site Görünüm "