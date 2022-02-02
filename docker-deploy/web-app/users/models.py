# 在model.py中创建数据表
from django.db import models
from django.contrib.auth.models import User

    # casacade :if the user delete, the profile delete
class Profile(models.Model):
    username= models.CharField(max_length=200,default='')
    vehicle_type_registered = models.CharField(max_length=200,default='')
    license_plate_number = models.CharField(max_length=200,default='')
    capacity_of_the_car = models.IntegerField()
    spacial_request = models.CharField(max_length=200,default='')


    def __str__(self):
        return f'{self.username} Profile'



