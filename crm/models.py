from django.db import models

# Create your models here.
class Player(models.Model):
  name=models.CharField(max_length=200)
  age=models.PositiveIntegerField()
  SPORTS_OPTION=[
    ('cricket','cricket'),
    ('football','football'),
    ('hockey','hockey'),
    ('chess','chess')
  ]
  sports=models.CharField(max_length=200,choices=SPORTS_OPTION,null=True)
  ranking=models.PositiveIntegerField()
  role=models.CharField(max_length=100)
