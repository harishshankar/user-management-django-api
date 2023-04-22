from django.db import models

# Create your models here.

class UserManagement(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mobile = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username 
