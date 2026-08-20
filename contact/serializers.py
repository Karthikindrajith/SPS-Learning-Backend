from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage

        fields = [
            "id",
            "full_name",
            "email",
            "phone_number",
            "subject",
            "message",
            "created_at",
            "is_read",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "is_read",
        ]

    def validate_full_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "Full name must contain at least 2 characters."
            )

        return value.strip()

    def validate_subject(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Subject must contain at least 3 characters."
            )

        return value.strip()

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Message must contain at least 10 characters."
            )

        return value.strip()

    def validate_phone_number(self, value):
        if value:
            value = value.strip()

            if not value.replace("+", "").replace(" ", "").isdigit():
                raise serializers.ValidationError(
                    "Enter a valid phone number."
                )

        return value