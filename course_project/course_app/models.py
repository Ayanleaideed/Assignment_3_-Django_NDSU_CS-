from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()
    instructor = models.CharField(max_length=100)
    start_date = models.DateField()
    prerequisites = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
