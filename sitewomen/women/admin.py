from django.contrib import admin
from .models import Women


admin.site.register(Women)
admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщины мира"

