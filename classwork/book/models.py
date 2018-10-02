import datetime
from django.db import models
from django.utils import timezone

class Book(models.Model):
    name_text = models.CharField(max_length=200)
    starBook.s_text = models.CharField(max_length=10)
    release_date = models.DateTimeField('date published')

