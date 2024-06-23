from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from .models import News

# Create your views here.



class NewsListView(ListView):
    model = News
    context_object_name = "news_objects"
    template_name = "news/list_news.html"
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            return News.objects.filter(title__icontains=query)
        
        return News.objects.all()


def news_topic_view(request, pk):
    news = News.objects.filter(news_type=pk)
    return render(request, "news/list_news.html", {"news_objects": news})


class NewsDetailView(DetailView):
    model = News
    context_object_name = "new"
    template_name = "news/detail_news.html"

    def get_context_data(self, **kwargs):
        
        news = self.get_object()
        news.views += 1
        news.save()

        return super().get_context_data(**kwargs)

