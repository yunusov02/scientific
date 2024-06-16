from django.db import models

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
    description = models.TextField()
    photo = models.ImageField(upload_to='news/', default='static/img/defalut.jpg')

    views = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']


    def __str__(self):
        return self.title[:50]
