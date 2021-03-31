from django.contrib import admin
from .models import Book, UsedBook, Category
# Register your models here.

admin.site.register(Book)
admin.site.register(UsedBook)
admin.site.register(Category)