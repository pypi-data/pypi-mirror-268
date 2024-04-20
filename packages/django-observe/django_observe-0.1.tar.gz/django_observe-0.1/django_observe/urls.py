from django.urls import path

from django_observe.views import glass

urlpatterns = [
    path("", glass),
]
