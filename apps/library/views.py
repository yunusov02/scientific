from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Library

# Create your views here.


class LibraryListView(ListView):
    model = Library
    context_object_name = "libraries_objects"
    template_name = "library/list_library.html"
    paginate_by = 15


    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            return Library.objects.filter(title__icontains=query)

        return Library.objects.all()


def library_topic_view(request, pk):
    libraries = Library.objects.filter(type=pk)
    return render(request, "library/list_library.html", {"libraries_objects": libraries})


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "lib"
    template_name = "library/detail_library.html"
    
    def get_context_data(self, **kwargs):
        
        library = self.get_object()
        library.views += 1
        library.save()

        return super().get_context_data(**kwargs)

