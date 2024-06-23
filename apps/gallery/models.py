from django.db import models

# Create your models here.



class Photo(models.Model):
    title = models.CharField(max_length=1023, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='gallery/')
    views = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']


    def __str__(self):
        return self.title[:50]


class Video(models.Model):
    title = models.CharField(max_length=1023)
    link = models.URLField(max_length=200, blank=True)
    views = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']


    def __str__(self):
        return self.title[:50]


