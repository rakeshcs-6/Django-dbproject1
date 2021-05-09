from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()
    marks=models.FloatField()
    def __str__(self):
        return self.name
