from django.db import models
from django.utils import timezone


class TimeStamp(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    state = models.BooleanField(default=False)


class WeeklyHourDefault(models.Model):
    weekly_hours = models.IntegerField(default=10)


class HourlyGoals(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    week_number = models.IntegerField(default=1)
    weekly_hours = models.IntegerField(default=1)
