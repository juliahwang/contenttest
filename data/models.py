from django.db import models


# Create your models here.


class Data(models.Model):
    used_date = models.CharField(max_length=50)
    line_num = models.CharField(max_length=10)
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=30)
    paid_on = models.PositiveIntegerField()
    paid_off = models.PositiveIntegerField()
    unpaid_on = models.PositiveIntegerField()
    unpaid_off = models.PositiveIntegerField()
    submit_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.station_name

    def get_selected_data(self):
        return {
            "paid_on": self.paid_on,
            "paid_off": self.paid_off,
            "unpaid_on": self.unpaid_on,
            "unpaid_off": self.unpaid_off
        }