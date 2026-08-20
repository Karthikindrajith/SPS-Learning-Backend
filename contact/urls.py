from django.urls import path
from .views import (
    ContactMessageCreateView,
    ContactMessageListView,
)

urlpatterns = [
    path(
        "send/",
        ContactMessageCreateView.as_view(),
        name="contact-send",
    ),

    path(
        "messages/",
        ContactMessageListView.as_view(),
        name="contact-messages",
    ),
]