from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="abouts/images",default=1)
    def __str__(self) -> str:
        return self.name
