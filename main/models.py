from django.db import models

# Create your models here.

class ContactForm(models.Model):
    NAME=models.CharField(max_length=20)
    EMAIL=models.EmailField()
    SUBJECT=models.CharField(max_length=50)
    MESSAGE=models.CharField(max_length=200)
    
    def __str__(self):
        return self.NAME
