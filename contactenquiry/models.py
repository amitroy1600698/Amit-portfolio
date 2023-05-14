from django.db import models

class contactenquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    message = models.TextField()
    

# Create your models here.
