from pickle import TRUE
from django.db import models

# Create your models here.
class Thing(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.name

