from django import forms
from django.forms import ModelForm
from .models import Books, Authors

class BookForm(ModelForm):
    # Define a ModelChoiceField for the 'author' field
    author = forms.ModelChoiceField(
        queryset=Authors.objects.all(),
        empty_label=None,  # Remove the default '---------' option
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Books
        fields = ('bookId', 'book_name','author_name', 'publisher', 'author', 'book_image')
        widgets = {
            'bookId': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kitap Adı'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Yazar Adı-Soyadı'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Yayınevi'})
        }
        labels = {
            'bookId': '',
            'book_name': '',
            'author_name': '',
            'author': '""',
            'publisher': '',
            'book_image': 'Resim Ekle',
        }
