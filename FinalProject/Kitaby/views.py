from django.shortcuts import render,redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login as auth_login
from .models import Book, UsedBook, OrderBook, Order
from django.contrib.auth import password_validation
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .forms import addUsedBookForm
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
User = get_user_model()

# Create your views here.


def Index(request):

    return render(request , 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, email=email,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'something went wrong try again')
            return redirect('login')
    else:
        return render(request, 'login.html')

def Registeration(request):
    if request.method == 'POST':
        FName = request.POST['FName']
        LName = request.POST['LName']
        email = request.POST['email']
        password = request.POST['password']
        ContactNo = request.POST['ContactNo']
        Address = request.POST['Address']
        Gender = request.POST['Gender']
        University = request.POST['University']
        Major = request.POST['Major']

        if User.objects.filter(email=email).exists():
            messages.info(request, "Alredy have account!")
            return redirect('Registeration')
        else:
            user = User.objects.create_user(email=email, password=password, FName=FName, 
            LName=LName,ContactNo=ContactNo, Address=Address, Gender=Gender, University=University, Major=Major)
            user.save()
            return redirect('/')
    else:
        return render(request, 'Registeration.html')

class Borrowing(ListView):
    model = Book
    template_name = "Borrowing.html"
    

class BuyBookView(ListView):
    model = Book
    template_name = "buyBook.html"

class BookDetails(DetailView):
    model = Book
    template_name = "BookDetails.html"


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            return redirect("/")
        



def Contact(request):
    if request.method == "POST":
        Msg_name = request.POST['Msg-name']
        Msg_email = request.POST['Msg-email']
        Msg_number = request.POST['Msg-number']
        Msg_message = request.POST['Msg-message']

        send_mail(
            'contact from ' + Msg_name,
            'email from ' + Msg_email + " " +
            Msg_message,
            Msg_email,
            ['adnan@bowxgames.com'],
        )
        return render(request, 'Contact.html' , {'Msg_name': Msg_name})
    else:
        return render(request, 'Contact.html')

def SellBook(request):
    context = {
        "usedBook" : UsedBook.objects.all()
    }

    return render(request, 'sellBook.html', context)


def addUsedBook(request):
    user = request.user
    if user is not None and user.is_active:
        form= addUsedBookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            Book_Image= request.FILES['Book_Image']
            fs= FileSystemStorage()
            fs.save(Book_Image.name, Book_Image)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/SellBook')
        context= {'form': form }
        return render(request, 'sellusedBook.html', context)
    else:
        return redirect('/login')
    
    
    #if request.method == 'POST':
        
        #return redirect('/SellBook')
    #else:
    

def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def add_in_cart(request,slug):
    book = get_object_or_404(Book, slug=slug)
    order_book, created = OrderBook.objects.get_or_create(
        book=book,
        user = request.user,
        ordered=False
            
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__slug=book.slug).exists():
            order_book.quantity += 1
            order_book.save()
            messages.info(request, "You add New Book")
        else:
            messages.info(request, "The book was orderd sucssefuly")
            order.books.add(order_book)
            return redirect("Kitaby:Details", slug=slug)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.books.add(order_book)
        messages.info(request, "The book was orderd sucssefuly")

        return redirect("Kitaby:Details", slug=slug)
    return redirect("Kitaby:Details", slug=slug)
@login_required
def remove_from_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__slug=book.slug).exists():
            order_book = OrderBook.objects.filter(
                book=book,
                user=request.user,
                ordered=False
            )[0]
            order.books.remove(order_book)
            messages.info(request, "The book was remove sucssefuly")
        else:
            messages.info(request, "The book was not in your cart")
            return redirect("Kitaby:Details", slug=slug)
            
    else:
        messages.info(request, "You don't have order")
        return redirect("Kitaby:Details", slug=slug)
    return redirect("Kitaby:Details", slug=slug)




def SearchBook(request):
    if request.method == "GET":
        SearchBook= request.GET.get('SearchBook')
        book = Book.objects.all().filter(Title=SearchBook)
        return render(request, 'SearchBook.html', {'book': book})


def load(request):
    return render(request, 'loading.html')

def bill(request):
    return render(request, 'bill.html')

def done(request):
    return render(request, 'done.html')