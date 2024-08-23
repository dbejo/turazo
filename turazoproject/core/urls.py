from django.urls import path
from . import views

urlpatterns = [
    path("", views.core_index, name="core_index"),
    path("cikk/<slug:slug>/", views.core_post, name="core_post"),
    path("kategoriak/<slug:slug>/", views.core_categories, name="core_categories"),
    path("ujdonsagok/", views.core_news, name="core_news")
]