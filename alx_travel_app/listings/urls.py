from django.urls import path
from . import views  # Ensure views.py exists

urlpatterns = [
    path("", views.sample_view, name="sample_view"),
]