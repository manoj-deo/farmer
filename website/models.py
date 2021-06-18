from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200)
    image= models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Orders(models.Model):
    name_o= models.CharField(max_length=200, null=True)
    description_o=models.CharField(max_length=200)
    def __str__(self):
        return self.name_o
