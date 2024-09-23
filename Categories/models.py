from django.db import models
# Create your models here.
class Categories(models.Model):
    name  = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/images",default=1)
    def __str__(self) -> str:
        return self.name