from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags

# Create your models here.


NEWS_TYPE = (
    (1, "Stipendiya e’lonlari"),
    (2, "Oliy ta’limdan keyingi ta’lim qabuli"),
    (3, "Malakaviy imtihon"),
    (4, "Himoya e’lonlari"),
    (5, "Doktorantlarni ilmiy seminar e’lonlari"),
    (6, "Konferensiya e’lonlari")
)


class News(models.Model):
    news_type = models.IntegerField(choices=NEWS_TYPE)
    title = models.CharField(max_length=1023)
    description = RichTextField()
    photo = models.ImageField(upload_to='news/', default='back1.jpg')
    min_desc = models.TextField(max_length=200, blank=True)  # yangi o'zgaruvchi
    views = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']


    def save(self, *args, **kwargs):
        # HTML teglarini olib tashlash
        plain_text = strip_tags(self.description)
        # Matnni 200 ta belgi bilan cheklash
        max_length = 100
        if len(plain_text) > max_length:
            self.min_desc = plain_text[:max_length]
        else:
            self.min_desc = plain_text
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title[:50]
