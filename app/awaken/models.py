import datetime

from django.db import models
from django.core.validators import int_list_validator
from django.contrib.auth.models import User

class Task(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    points = models.IntegerField()

class Points(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    last_reset = models.DateField(default=datetime.date.today)
    weekly_points = models.IntegerField(default=0)
    daily_points = models.IntegerField(default=0)
    data_points = models.CharField(
        validators=[int_list_validator],
        max_length=100,
        default="0,0,0,0,0,0,0,0,0,0,0,0,0,0"
    )
