from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    Your_Name = models.CharField(max_length=50)
    Your_Email = models.EmailField(max_length=200)
    Subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=1000)

    def __str__(self):
        return self.Your_Name
