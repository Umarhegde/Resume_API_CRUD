from django.db import models
 
# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    position = models.CharField(max_length=100)    

    def __str__(self):
        return self.name
     
