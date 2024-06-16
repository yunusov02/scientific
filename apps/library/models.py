from django.db import models
from apps.base.models import Department
# Create your models here.



class Library(models.Model):
    JOB_TITLE = (
        (1, 'Talaba'),
        (2, 'Professor'),
    )

    DOCUMENT_TYPE = (
        (1, 'Avtoreferat'),
        (2, 'Maqola'),
        (3, "Konferensiya to'plamlari"),
        (4, "Talabalar to'plamlari"),
        (5, "Monografiya"),
    )

    type = models.IntegerField(choices=DOCUMENT_TYPE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    full_name = models.CharField(max_length=255)
    job_title = models.IntegerField(choices=JOB_TITLE)

    title = models.CharField(max_length=1023)
    description = models.TextField()
    pdf = models.FileField(upload_to='documents/')

    views = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_date']


    def __str__(self):
        return self.title[:50]


