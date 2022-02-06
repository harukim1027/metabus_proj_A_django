from django.contrib import admin
from streetanimal.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["animal_no", "sex", "date_of_discovery", "start_date", "end_date"]
    list_display_links = ["animal_no"]
    search_fields = ["animal_no"]
