from django import forms
from authors.models import Place, Author, Book


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
