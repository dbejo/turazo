from django.urls import path
from . import views

urlpatterns = [
    path("", views.core_index, name="core_index"),
    path("cikk/<slug:slug>/", views.core_post, name="core_post")
]