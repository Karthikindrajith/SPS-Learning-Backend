from rest_framework import serializers

from .models import Career


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career

        fields = [
            "id",
            "title",
            "company",
            "department",
            "location",
            "employment_type",
            "experience",
            "salary",
            "skills",
            "description",
            "requirements",
            "responsibilities",
            "is_active",
            "posted_date",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "posted_date",
            "created_at",
            "updated_at",
        ]

    def validate_skills(self, value):
        if value is None:
            return []

        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Skills must be a list."
            )

        return value