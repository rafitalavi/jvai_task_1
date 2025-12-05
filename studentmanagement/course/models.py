from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank = True , null = True)
    def __str__(self):
        return self.name
