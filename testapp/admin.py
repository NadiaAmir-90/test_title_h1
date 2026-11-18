
from django.contrib import admin
from .models import Results


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "bs4_title",
        "playwright_title",
        "title_passed",
        "bs4_h1",
        "playwright_h1",
        "h1_passed",
    )

    search_fields = (
        "site_name",
        "bs4_title",
        "playwright_title",
        "bs4_h1",
        "playwright_h1",
    )

    readonly_fields = ()
