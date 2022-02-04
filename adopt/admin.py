from django.contrib import admin
from adopt.models import Review

@admin.register(Review)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "nickname"]
    list_display_links = ["title"]
    search_fields = ["title"]