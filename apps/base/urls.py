from django.urls import path, include

from .views import home_page, faoliyat


urlpatterns = [
    path("", home_page, name="home_page"),
    path("faoliyat/", faoliyat, name="faoliyat"),
]


