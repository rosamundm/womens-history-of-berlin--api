from django.contrib import admin
from .models import TextPage


@admin.register(TextPage)
class TextPageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "slug"
    )
