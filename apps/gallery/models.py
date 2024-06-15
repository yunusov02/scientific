from django.db import models

# Create your models here.



class Photo(models.Model):
    title = models.CharField(max_length=1023)
    description = models.TextField()
    photo = models.ImageField(upload_to='gallery/')
    views = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']


    def __str__(self):
        return self.title[:50]


class Video(models.Model):
    title = models.CharField(max_length=1023)
    link = models.URLField(max_length=200, blank=True)
    views = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']


    def __str__(self):
        return self.title[:50]


