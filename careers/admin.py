from django.contrib import admin

from .models import Career


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "department",
        "location",
        "employment_type",
        "experience",
        "salary",
        "is_active",
        "posted_date",
    )

    list_filter = (
        "department",
        "employment_type",
        "is_active",
        "posted_date",
    )

    search_fields = (
        "title",
        "company",
        "department",
        "location",
        "experience",
        "salary",
    )

    list_editable = (
        "is_active",
    )

    readonly_fields = (
        "posted_date",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-posted_date",
    )

    fieldsets = (
        (
            "Job Information",
            {
                "fields": (
                    "title",
                    "company",
                    "department",
                    "location",
                    "employment_type",
                    "experience",
                    "salary",
                )
            },
        ),
        (
            "Skills",
            {
                "fields": (
                    "skills",
                )
            },
        ),
        (
            "Job Description",
            {
                "fields": (
                    "description",
                    "requirements",
                    "responsibilities",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "posted_date",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )