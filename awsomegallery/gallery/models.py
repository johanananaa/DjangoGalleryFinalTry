from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
