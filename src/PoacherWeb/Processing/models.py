from django.db import models

# Create your models here.
class PoacherImage(models.Model):
    ImageName = models.CharField(max_length = 100)
    Image = models.ImageField(upload_to='images/')
