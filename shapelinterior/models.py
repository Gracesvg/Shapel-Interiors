from django.db import models


# Create your models here.

class project(models.Model):
    pname = models.CharField(max_length=30)
    pcoordiator = models.CharField(max_length=20)
    pdate = models.DateField(max_length=10)
    pduration = models.DurationField()
    pupdates = models.CharField(max_length=10)

class Meta:
    db_table = 'project'