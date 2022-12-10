from django.contrib import admin
from .models import Gallery

class galleryAdmin(admin.ModelAdmin):
    readonly_fields = ()

admin.site.register(Gallery, galleryAdmin)