from django.db import models

from careers.models import Career


class CareerApplication(models.Model):
    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Shortlisted", "Shortlisted"),
        ("Interview", "Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]

    job = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    full_name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20
    )

    location = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    experience = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    resume = models.FileField(
        upload_to="resumes/"
    )

    cover_letter = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Applied",
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"

    class Meta:
        ordering = ["-applied_at"]