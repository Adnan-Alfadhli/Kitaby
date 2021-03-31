from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index ,name= "Index"),
    path('login', views.Login, name= "Login"),
    path('Registeration', views.Registeration, name= "Registeration"),
    path('Borrowing', views.Borrowing, name= "Borrowing"),
    path('BuyBook', views.BuyBook, name= "BuyBook"),
    path('Contact', views.Contact, name= "Contact"),
    path('SellBook', views.SellBook, name= "SellBook"),
    
]