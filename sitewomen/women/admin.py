from django.contrib import admin

from .models import Category, Women

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщины мира"


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published", "cat")
    list_display_links = ("id", "title")
    ordering = ("time_create", "title")
    list_editable = ("is_published",)
    list_per_page = 5


@admin.register(Category)
class CanegoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


# admin.site.register(Women, WomenAdmin)
