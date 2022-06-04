from pickle import TRUE
from urllib import request
from django.db import models
from django.contrib.auth import get_user_model

#ObjectModel


# Create your models here.
class ObjectModel(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    user= models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=1)
    


    def __str__ (self):
        return self.name

