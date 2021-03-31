from django.shortcuts import render

# Create your views here.
def Index(request):

    return render(request , 'index.html')

def Login(request):

    return render(request, 'login.html')

def Registeration(request):

    return render(request, 'Registeration.html')

def Borrowing(request):

    return render(request, 'Borrowing.html')

def BuyBook(request):

    return render(request, 'buyBook.html')

def Contact(request):

    return render(request, 'Contact.html')

def SellBook(request):

    return render(request, 'sellBook.html')