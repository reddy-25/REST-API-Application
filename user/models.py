from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class advisor(models.Model):
    advisor_name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=150)


class booking(models.Model):
    advisor_name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=150)
    advisor_id = models.IntegerField()
    booking_time = models.CharField(max_length=50)
    user = models.IntegerField()
