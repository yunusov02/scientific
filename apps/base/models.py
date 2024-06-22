from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return f"{self.name} {self.email}"


