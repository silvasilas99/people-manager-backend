from django.db import models

class Person (models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Birthday = models.DateTimeField()
    Cpf =  models.IntegerField()
    Gender = models.CharField(max_length=50)
    Height = models.DecimalField(max_length=10, max_digits=8, decimal_places=2)
    Weight = models.DecimalField(max_length=10, max_digits=8, decimal_places=2)
