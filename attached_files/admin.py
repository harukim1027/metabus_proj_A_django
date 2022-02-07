from django.contrib import admin
from attached_files.models import Attached_file


@admin.register(Attached_file)
class AttachedFileAdmin(admin.ModelAdmin):
    list_display = ["notice_no", "att_file_no"]
    list_display_links = ["att_file_no"]
    search_fields = ["att_file_no"]

