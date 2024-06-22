from django.urls import path

from .views import NewsDetailView, NewsListView, news_topic_view


urlpatterns = [
    path("news-list/", NewsListView.as_view(), name="news_list"),
    path("news_topic_view/<int:pk>", news_topic_view, name="news_topic"),
    path("news-detail/<int:pk>", NewsDetailView.as_view(), name="news-detail")
]


