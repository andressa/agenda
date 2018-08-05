from django.db import models
from datetime import datetime

class Meeting(models.Model):

    name = models.CharField(max_length=30, blank=False)
    date = models.DateTimeField(blank=False)

    def __str__(self):
        return "{} at {}".format(
            name,
            date.strftime("%d-%b-%Y %H:%M")
        )
