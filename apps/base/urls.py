from django.urls import path, include

from .views import home_page, faoliyat, contactus


urlpatterns = [
    path("", home_page, name="home_page"),
    path("faoliyat/", faoliyat, name="faoliyat"),
    path("contactus/", contactus, name="contactus"),
]


