from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=500)
    decs = models.TextField(max_length= 200000000)
    date_of_post = models.DateTimeField(datetime.now(), blank=True)
