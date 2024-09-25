from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.TextField()
    email=models.CharField(max_length=200)
    message=models.TextField()
    
    def __str__(self) -> str:
            return self.name