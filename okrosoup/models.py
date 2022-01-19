from django.db import models

import okrosoup

# Create your models here
Class todo(models.Model):
    text= models.CharField(max_length=40)
    complete = models.BooleanField(default=False) 
    date = models.dateTimeField(auto_now_add=True)
    
    def __str__(self):
    return self.text
    



