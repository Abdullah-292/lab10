from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)
    
    
class Address(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    adress = models.ForeignKey(Address,on_delete=models.CASCADE)
    
    
    
  
class Student2(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    addresses  = models.ManyToManyField(Address)
    
    
class BookCover(models.Model):
    title = models.CharField(max_length = 50)
    coverPage = models.ImageField(upload_to='documents/')