from django.db import models

class ScrapModel(models.Model):
    date=models.DateField()
    open_filed=models.FloatField()
    hight_field=models.FloatField()
    low_field=models.FloatField()
    close_field=models.FloatField()
    adj_close_field=models.FloatField()
    volume_field=models.FloatField()
    name=models.CharField(max_length=10)
