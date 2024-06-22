from django.urls import path

from .views import LibraryListView, LibraryDetailView, library_topic_view


urlpatterns = [
    path("library-list/", LibraryListView.as_view(), name="library_list"),
    path("library_topic/<int:pk>", library_topic_view, name="library_topic"),
    path("library-detail/<int:pk>", LibraryDetailView.as_view(), name="library_deatil")
]


