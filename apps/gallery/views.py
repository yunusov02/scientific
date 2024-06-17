from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo, Video

# Create your views here.



class PhotoListView(ListView):
    model = Photo
    context_object_name = "photos"
    template_name = "gallery/list_photo.html"


class PhotoDetailView(DetailView):
    model = Photo
    context_object_name = "photo"
    template_name = "gallery/detail_photo.html"



class VideoListView(ListView):
    model = Video
    context_object_name = "videos"
    template_name = "gallery/list_video.html"


class VideoDetailView(DetailView):
    model = Video
    context_object_name = "video"
    template_name = "gallery/detail_photo.html"


