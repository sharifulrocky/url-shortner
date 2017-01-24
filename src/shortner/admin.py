from django.contrib import admin

from .models import ShortUrl


class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortcode', 'active', 'timestamp', 'update')
    list_display_links = ('url', 'shortcode', )
    list_filter = ('active', 'timestamp', 'update')
    search_fields = ('url', 'shortcode')
    list_per_page = 5

admin.site.register(ShortUrl, UrlAdmin)