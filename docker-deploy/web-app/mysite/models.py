from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    special_request = models.TextField()
    post_required_date = models.DateTimeField(default=timezone.now)
    # delete 当用户删除post之后
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Ride(models.Model):
    owner = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    status = models.IntegerField()
    party = models.IntegerField()
    destination = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(default=timezone.now)
    to_join = models.BooleanField()
    # Optional
    special_info = models.CharField(max_length=100, blank=True)
    vehicle_type = models.CharField(max_length=100, blank=True)
    total_pp = models.IntegerField()
    def get_email(self):
        return self.owner.email

class Sharer(models.Model):
    ride_id = models.IntegerField()
    sharer = models.CharField(max_length=100)
    party = models.IntegerField()