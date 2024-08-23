from django.urls import path
from . import views

urlpatterns = [
    path("", views.core_index, name="core_index"),
    path("cikk/<int:year>/<int:month>/<int:day>/<slug:slug>/", views.core_post, name="core_post"),
    path("cikk/<int:year>/<int:month>/<int:day>/", views.core_day, name="core_post_day"),
    path("cikk/<int:year>/<int:month>/", views.core_month),
    path("cikk/<int:year>/", views.core_year),
    path("cikk/", views.redirect_view),
    path("kategoriak/<slug:slug>/", views.core_categories, name="core_categories"),
    path("cimkek/<slug:slug>/", views.core_tags, name="core_tags"),
    path("cimkek/", views.redirect_view),
    path("ujdonsagok/", views.core_news, name="core_news")
]