from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from authors.forms import PlaceForm, AuthorForm, BookForm
from authors.models import Place, Author, Book

#@permission_required("authors.add_place") #name seen in the admin available permissions section: syntax is app, permission and lower case name of model 
@login_required
def create_place_view(request):
    place_list = Place.objects.all()
    place_form = PlaceForm()
    if request.POST:
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
            return redirect("place_create")
    return render_to_response("create_place.html", RequestContext(request, {
        "place_list": place_list,
        "place_form": place_form
    }))

def edit_place_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_list = Place.objects.all()
    place_form = PlaceForm(instance=place)
    if request.POST:
        place_form = PlaceForm(request.POST, instance=place)
        if place_form.is_valid():
            place_form.save()
            return redirect("place_create")
    return render_to_response("create_place.html", RequestContext(request, {
        "place_list": place_list,
        "place_form": place_form,
        "is_edit": True,
    }))

def delete_place_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place.delete()
    return redirect("place_create")

def create_author_view(request):
    author_list = Author.objects.all()
    author_form = AuthorForm()
    if request.POST:
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("create_author")
    return render_to_response("create_author.html", RequestContext(request, {
        "author_list": author_list,
        "author_form": author_form,
        }))

def edit_author_view(request, author_id):
    author_list = Author.objects.get(id=author_id)
    author_form = AuthorForm(instance=author_list)
    if request.POST:
        author_form = AuthorForm(request.POST, instance=author_list)
        if author_form.is_valid():
            author_form.save()
            return redirect("create_author")
    return render_to_response("edit_author.html", RequestContext(request, {
        "author_list": author_list,
        "author_form": author_form,
        }))

def create_book_view(request):
    book_list = Book.objects.all()
    book_form = BookForm()
    if request.POST:
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("create_book")
    return render_to_response("create_book.html", RequestContext(request, {
        "book_list": book_list,
        "book_form": book_form,
        }))

def edit_book_view(request, book_id):
    book_list = Book.objects.get(id=book_id)
    book_form = BookForm(instance=book_list)
    if request.POST:
        book_form = BookForm(request.POST, instance=book_list)
        if book_form.is_valid():
            book_form.save()
            return redirect("create_book")
    return render_to_response("edit_book.html", RequestContext(request, {
        "book_list": book_list,
        "book_form": book_form,
        }))




