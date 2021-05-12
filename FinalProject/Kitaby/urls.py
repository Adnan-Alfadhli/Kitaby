from django.contrib import admin
from django.urls import path
from . import views


app_name = 'Kitaby'

urlpatterns = [
    path('', views.Index ,name= "Index"),
    path('login', views.login, name= "login"),
    path('Registeration', views.Registeration, name= "Registeration"),
    path('Borrowing', views.Borrowing.as_view(), name= "Borrowing"),
    path('BuyBook', views.BuyBookView.as_view(), name= "BuyBook"),
    path('Contact', views.Contact, name= "Contact"),
    path('SellBook', views.SellBook, name= "SellBook"),
    path('logout', views.logout, name= "logout"),
    path('addUsedBook', views.addUsedBook, name= "addUsedBook"),
    path('Details/<slug>/', views.BookDetails.as_view(), name="Details"),
    path('add-to-cart/<slug>/', views.add_in_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name="remove-from-cart"),
    path('SearchBook/', views.SearchBook, name="SearchBook"),
    path('OrderSummaryView/', views.OrderSummaryView.as_view(), name="OrderSummaryView"),
    path('load', views.load, name="load"),
    path('bill/', views.bill, name="bill")
    
]