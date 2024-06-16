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
        topic = self.request.GET.get('topic')
        if query:
            return Library.objects.filter(title__icontains=query)
        
        if topic:
            return Library.objects.filter(document_type=topic)

        return Library.objects.all()



class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"
    template_name = "library/detail_library.html"
    
    def get_context_data(self, **kwargs):
        
        library = self.get_object()
        library.views += 1
        library.save()

        super().get_context_data(**kwargs)

