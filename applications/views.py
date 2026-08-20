from rest_framework import generics
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
)

from .models import CareerApplication
from .serializers import CareerApplicationSerializer


class CareerApplicationCreateView(
    generics.CreateAPIView
):
    queryset = CareerApplication.objects.all()

    serializer_class = (
        CareerApplicationSerializer
    )

    parser_classes = [
        MultiPartParser,
        FormParser,
    ]


class CareerApplicationListView(
    generics.ListAPIView
):
    queryset = CareerApplication.objects.all()

    serializer_class = (
        CareerApplicationSerializer
    )