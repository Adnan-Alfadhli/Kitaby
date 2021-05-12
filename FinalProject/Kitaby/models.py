from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.conf import settings
from django.shortcuts import reverse
class UserManager(BaseUserManager):
    def create_user(self, email, password =None, FName= None, LName=None,ContactNo=None,
    Address=None,Gender=None, University=None,Major=None,is_active = True, is_staff = False ,is_admin=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must hhave password")
        user = self.model(
            email = self.normalize_email(email),
            FName = FName,
            LName = LName,
            ContactNo = ContactNo,
            Address = Address,
            Gender = Gender,
            University = University,
            Major = Major

        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user 
    def create_staffuser(self, email, password=None,FName= None, LName=None,ContactNo=None
    ,Address=None,Gender=None, University=None,Major=None):
        user = self.create_user(
                email,
                FName = FName,
                LName = LName,
                ContactNo = ContactNo,
                Address = Address,
                Gender = Gender,
                University = University,
                Major = Major,
                password=password,
                is_staff=True
        )
        return user
    def create_superuser(self, email,password=None,FName= None, LName=None,ContactNo=None,
    Address=None,Gender=None, University=None,Major=None):
        user = self.create_user(
            email,
            FName = FName,
            LName = LName,
            ContactNo = ContactNo,
            Address = Address,
            Gender = Gender,
            University = University,
            Major = Major,
            password=password,
            is_admin = True,
            is_staff = True
        )
        return user

class User(AbstractBaseUser):
    email=models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default= True)
    staff = models.BooleanField(default= False)
    admin = models.BooleanField(default= False)
    FName=models.CharField(max_length=60, blank=True, null=True)
    LName=models.CharField(max_length=60, blank=True, null=True)
    ContactNo=models.IntegerField(blank=True, null=True)
    Address=models.CharField(max_length=255, blank=True, null=True)
    Gender=models.CharField(max_length=10, blank=True, null=True)
    University=models.CharField(max_length=255, blank=True, null=True)
    Major=models.CharField(max_length=255, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj =None):
        return True
    def has_module_perms(self, app_label):
        return True

    def get_FName(self):
        if self.FName:
            return self.FName
        return self.email

    def get_LName(self):
        if self.LName:
            return self.LName
        return self.email

    def get_ContactNo(self):
        if self.ContactNo:
            return self.ContactNo
        return self.email

    def get_Address(self):
        if self.Address:
            return self.Address
        return self.email   

    def get_Gender(self):
        if self.Gender:
            return self.Gender
        return self.email   
    def get_University(self):
        if self.University:
            return self.University
        return self.email   

    def get_Major(self):
        if self.Major:
            return self.Major
        return self.email   
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
Category_Choices = (
    ('NEW','New'),
    ('RENT','Rent'),
    ('MOE','MOE')
)
class Book(models.Model):
    BookID=models.IntegerField(primary_key=True, unique=True )
    Title=models.CharField(max_length=60)
    ISBN=models.IntegerField()
    Price=models.IntegerField()
    Language=models.CharField(max_length=60)
    Publisher=models.CharField(max_length=60)
    CategoryType = models.CharField(choices=Category_Choices, max_length=4)
    slug = models.SlugField()
    Book_Image = models.ImageField(null=True , blank=True)
    #category
    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("Kitaby:Details", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("Kitaby:remove-from-cart", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("Kitaby:add-to-cart", kwargs={
            'slug': self.slug
        })

class UsedBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    BookID = models.AutoField(primary_key=True)
    Book_Image = models.ImageField(null=True , blank=True)
    Book_Title=models.CharField(max_length=60)
    Book_Price=models.IntegerField()
    
    
    def __str__(self):
        return self.Book_Title

    
class Category(models.Model):
    CategoryID=models.IntegerField(primary_key=True, unique=True )
    CategoryName=models.CharField(max_length=60)


class OrderBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity =models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.book.Title}"


    def get_total_book_price(self):
        return self.quantity * self.book.Price

    def get_final_price(self):
        return self.get_total_book_price()

class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    books = models.ManyToManyField(OrderBook)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.user.email

    def get_total(self):
        total = 0
        for order_book in self.books.all():
            total += order_book.get_final_price()
        return total

#Employee
#class Bag(models.Model):
    
#Catg 
#check if password at least 8