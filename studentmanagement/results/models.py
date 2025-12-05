from django.db import models
from student.models import Student
from course.models import Course

# Create your models here.
class Result(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE , related_name='results')
    subject = models.ForeignKey(Course , on_delete=models.CASCADE , related_name='results')
    marks_obtained = models.FloatField()
    def __str__(self):
        return f"{self.student.name} - {self.subject.name} : {self.marks_obtained}"