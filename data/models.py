from django.db import models


# Create your models here.
class Data(models.Model):
    used_date = models.DateTimeField()
    line_num = models.CharField(max_length=10)
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=30)
    paid_on = models.PositiveIntegerField()
    paid_off = models.PositiveIntegerField()
    unpaid_on = models.PositiveIntegerField()
    unpaid_off = models.PositiveIntegerField()
    submit_date = models.DateTimeField()
