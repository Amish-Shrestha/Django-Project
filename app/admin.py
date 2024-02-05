from django.contrib import admin
from django.db import models
# Register your models here.

class SiteConfiguration(models.Model):
    enable_feature = models.BooleanField(default=False)

class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ['enable_feature']
    
admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
