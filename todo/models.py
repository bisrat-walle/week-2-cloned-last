from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date_created = models.DateTimeField()

    def __str__(self):
        return self.title
