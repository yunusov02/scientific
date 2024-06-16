from django.urls import path

from .views import PhotoListView, PhotoDetailView, VideoListView, VideoDetailView


urlpatterns = [
    path("photo-list/", PhotoListView.as_view(), name="photo_list"),
    path("photo-detail/<int:pk>", PhotoDetailView.as_view(), name="photo_deatil"),

    path("video-list/", VideoListView.as_view(), name="video_list"),
    path("video-detail/<int:pk>", VideoDetailView.as_view(), name="video_deatil")
]


