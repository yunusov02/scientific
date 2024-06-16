from django.urls import path

from .views import NewsDetailView, NewsListView


urlpatterns = [
    path("news-list/", NewsListView.as_view(), name="news_list"),
    path("news-detail/<int:pk>", NewsDetailView.as_view(), name="news_deatil")
]


