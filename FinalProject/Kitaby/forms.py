from django import forms
from .models import UsedBook

class addUsedBookForm(forms.ModelForm):
    class Meta:
        model= UsedBook
        fields= ["BookID", "Book_Image", "Book_Title", "Book_Price"]