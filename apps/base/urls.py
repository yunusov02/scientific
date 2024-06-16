from django.urls import path, include

from .views import home_page, faoliyat


urlpatterns = [
    path("", home_page, name="home_page"),
    path("gallery/", include("apps.gallery.urls")),
    path("library/", include("apps.library.urls")),
    path("news/", include("apps.news.urls")),
    path("faoliyat/", faoliyat, name="faoliyat"),
]


