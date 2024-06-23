from django.shortcuts import render, redirect
from django.db.models import Sum
from django.views.generic import View, ListView
from django.contrib import messages

from apps.library.models import Library
from apps.news.models import News
from apps.gallery.models import Photo, Video
from .forms import ContactUsForm

from .config import CURRENT_MONTH, CURRENT_YEAR
# Create your views here.


def home_page(request):

    last_three_library = Library.objects.all()[:3]
    last_three_news = News.objects.all()[:3]

    total_count_library = Library.objects.all().count()
    total_count_views = Library.objects.aggregate(Sum('views'))['views__sum']

    current_month_upload_views = Library.objects.filter(added_date__month=CURRENT_MONTH, added_date__year=CURRENT_YEAR).aggregate(Sum('views'))['views__sum']
    current_month_upload_count = Library.objects.filter(added_date__month=CURRENT_MONTH, added_date__year=CURRENT_YEAR).count()

    last_five_photo = Photo.objects.all()[:5]
    last_three_video = Video.objects.all()[:3]

    context = {
        "last_three_library": last_three_library,
        "last_three_news": last_three_news,
        "total_count_library": total_count_library,
        "total_count_views": total_count_views,
        "current_month_upload_views": current_month_upload_views,
        "current_month_upload_count": current_month_upload_count,
        "last_five_photo": last_five_photo,
        "last_three_video": last_three_video
    }


    return render(request, "home.html", context=context)


def faoliyat(request):
    return render(request, "faoliyat-details.html")


def contactus(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabar jo'natildi.")
            return redirect('contactus')
        else:
            return render(request, 'blog/post_form.html', {'form': form})


    return render(request, "contact.html")

