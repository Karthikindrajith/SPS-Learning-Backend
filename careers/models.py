from django.db import models


class Career(models.Model):
    EMPLOYMENT_CHOICES = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Internship", "Internship"),
        ("Contract", "Contract"),
        ("Freelance", "Freelance"),
    ]

    title = models.CharField(
        max_length=200
    )

    company = models.CharField(
        max_length=200,
        default="SPS Solutions"
    )

    department = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=200
    )

    employment_type = models.CharField(
        max_length=50,
        choices=EMPLOYMENT_CHOICES,
        default="Full Time"
    )

    experience = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    salary = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    skills = models.JSONField(
        default=list,
        blank=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    requirements = models.TextField(
        blank=True,
        null=True
    )

    responsibilities = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    posted_date = models.DateTimeField(
        auto_now_add=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return self.title