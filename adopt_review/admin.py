from django.contrib import admin
from adopt_review.models import Review


@admin.register(Review)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["user", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]

