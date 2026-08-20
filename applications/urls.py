from django.urls import path

from .views import (
    CareerApplicationCreateView,
    CareerApplicationListView,
)


urlpatterns = [
    path(
        "",
        CareerApplicationCreateView.as_view(),
        name="career-application-create",
    ),

    path(
        "all/",
        CareerApplicationListView.as_view(),
        name="career-application-list",
    ),
]