from django.contrib import admin

from manageraccounts.models import ManagerAcc


@admin.register(ManagerAcc)
class ManagerAccAdmin(admin.ModelAdmin):
    list_display = ["admin_id"]
    list_display_links = ["admin_id"]
    search_fields = ["admin_id"]

