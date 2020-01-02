from django.contrib import admin

from .models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_hash', 'url', 'date_added', 'clicks', 'repeat_addition', 'last_ip')
    list_display_links = ('url_hash',)
    list_filter = ('date_added', 'clicks', 'last_ip')
    search_fields = ('url',)
    list_per_page = 25

admin.site.register(Url, UrlAdmin)
