from django.contrib import admin
from attached_images.models import Images


@admin.register(Images)
class AttachedImagesAdmin(admin.ModelAdmin):
    list_display = ["image_no"]
    list_display_links = ["image_no"]
    search_fields = ["image_no"]

