from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=100)
    slocation = models.CharField(max_length=100)
    semail = models.EmailField(max_length=100,unique=True)
    sage = models.IntegerField()
    def __str__(self):
        return self.sname

