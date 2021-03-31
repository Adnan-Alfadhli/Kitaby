from django.db import models

# Create your models here.
class Book(models.Model):
    BookID=models.IntegerField(primary_key=True, unique=True )
    Title=models.CharField(max_length=60)
    ISBN=models.IntegerField()
    Price=models.IntegerField()
    Language=models.CharField(max_length=60)
    Publisher=models.CharField(max_length=60)

class UsedBook(models.Model):
    BookID=models.IntegerField(primary_key=True, unique=True )
    Title=models.CharField(max_length=60)
    Price=models.IntegerField()
    #Seller

class Category(models.Model):
    CategoryID=models.IntegerField(primary_key=True, unique=True )
    CategoryName=models.CharField(max_length=60)
#Student
#Employee
#class Bag(models.Model):
    
#Catg 
     