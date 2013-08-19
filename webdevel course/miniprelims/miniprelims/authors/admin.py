from django.contrib import admin
from authors.models import Place, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Place, PlaceAdmin)
