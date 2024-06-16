from django.urls import path

from .views import LibraryListView, LibraryDetailView


urlpatterns = [
    path("library-list/", LibraryListView.as_view(), name="library_list"),
    path("library-detail/<int:pk>", LibraryDetailView.as_view(), name="library_deatil")
]


