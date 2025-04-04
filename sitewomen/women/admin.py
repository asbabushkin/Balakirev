from django.contrib import admin, messages

from .models import Category, Women

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщины мира"


class MarriedFilter(admin.SimpleListFilter):
    title = "Статус женщин"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ("married", "Замужем"),
            ("single", "Не замужем"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        elif self.value() == "single":
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
# редактирование записи
    fields = ["title", "content", "slug", "cat", "husband", "tags"]
#    readonly_fields = ["slug"] нередактируемое в режиме редактирования поле
    prepopulated_fields = {"slug": ("title", )}
    filter_vertical = ["tags"]
#    filter_horizontal = ["tags"]

# отображение списков
    list_display = ("title", "time_create", "is_published", "cat", "brief_info")
    list_display_links = ("title",)
    ordering = ("time_create", "title")
    list_editable = ("is_published",)
    list_per_page = 5
    actions = ("set_published", "set_draft")
    search_fields = ("title__startswith", "cat__name")
    list_filter = (MarriedFilter, "cat__name", "is_published")

    @admin.display(
        description="Краткое описание", ordering="content"
    )  # добавление столбца, которого нет в бд
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов."

    @admin.action(description="Опубликовать выбранные записи")  # добавления действия
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Опубликовано {count} записей.")

    @admin.action(
        description="Снять с публикации выбранные записи"
    )  # добавления действия
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(
            request, f"{count} записей снято с публикации.", messages.WARNING
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")