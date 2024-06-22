from apps.news.models import NEWS_TYPE
from apps.library.models import Library

def navbar_choices(request):
    news = NEWS_TYPE
    library = Library.DOCUMENT_TYPE

    return {
        "news": news,
        "libraries": library
    }
