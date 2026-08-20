from rest_framework import serializers

from .models import CareerApplication


class CareerApplicationSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = CareerApplication

        fields = [
            "id",
            "job",
            "full_name",
            "email",
            "phone",
            "location",
            "experience",
            "resume",
            "cover_letter",
            "status",
            "applied_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "applied_at",
            "updated_at",
        ]

    def validate_resume(self, value):
        allowed_extensions = [
            ".pdf",
            ".doc",
            ".docx",
        ]

        file_name = value.name.lower()

        if not any(
            file_name.endswith(ext)
            for ext in allowed_extensions
        ):
            raise serializers.ValidationError(
                "Only PDF, DOC and DOCX files are allowed."
            )

        max_size = 5 * 1024 * 1024

        if value.size > max_size:
            raise serializers.ValidationError(
                "Resume size must be less than 5 MB."
            )

        return value