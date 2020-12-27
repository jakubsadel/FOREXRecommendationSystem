from django.db import models

# Create your models here.

class Stock(models.Model):
    today_date = models.DateField()
    previous_date = models.DateField()
