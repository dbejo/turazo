from django.urls import path
from . import views

urlpatterns = [
    path("", views.core_index, name="core_index")
]