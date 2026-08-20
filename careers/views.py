from rest_framework import generics

from .models import Career
from .serializers import CareerSerializer


class CareerListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = CareerSerializer

    def get_queryset(self):
        return Career.objects.filter(
            is_active=True
        ).order_by("-posted_date")


class CareerDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer