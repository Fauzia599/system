from django.db import models
from django.utils import timezone

# Create your models here.
class Cleaner(models.Model):
    Name = models.CharField(max_length=100)
    Contact_Info = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)  # "Admin" or "Cleaner"
    issues = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.Name}"
    
class Task(models.Model):
    Description = models.TextField()
    Status = models.CharField(max_length=100)  
    Date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.task_name}"
        
class Facility(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=200)
    Description = models.TextField()


    def __str__(self):
        return f"{self.Name}"