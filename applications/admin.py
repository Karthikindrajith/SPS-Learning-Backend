from django.contrib import admin

from .models import CareerApplication


@admin.register(CareerApplication)
class CareerApplicationAdmin(
    admin.ModelAdmin
):
    list_display = (
        "full_name",
        "job",
        "email",
        "phone",
        "experience",
        "status",
        "applied_at",
    )

    list_filter = (
        "status",
        "applied_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "job__title",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "applied_at",
        "updated_at",
    )

    ordering = (
        "-applied_at",
    )