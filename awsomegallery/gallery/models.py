from django.db import models

# Create your models here.
class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
