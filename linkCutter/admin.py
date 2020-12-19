from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['creator', 'source_link', 'clicks']
    list_filter = ['creator']
