from django.urls import path
from . import views

urlpatterns = [
    path("", views.vehicels_index, name="vehicels_index"),
    path("<int:pk>/", views.vehicel_detail, name="vehicel_detail"),
]