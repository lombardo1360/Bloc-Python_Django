from distutils.command import upload
from django.db import models
import  datetime

class Post(models.Model):
    title_post   = models.CharField(max_length=100)
    descriptions = models.TextField()
    images       = models.ImageField(upload_to="blog/images")
    date_time    = models.DateField(datetime.date.today)
