from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Book, UsedBook, Category, OrderBook, Order
# Register your models here.

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = User
admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(UsedBook)
admin.site.register(Category)
admin.site.register(OrderBook)
admin.site.register(Order)