from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=50, unique=True)
    age = models.IntegerField(blank=True, null=True)
    mail = models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.name