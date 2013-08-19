from django.conf.urls import patterns, include, url


urlpatterns = patterns('authors.views',

    url(r'^places/new/', 'create_place_view', name="place_create"),

    url(r'^places/edit/(?P<place_id>\d+)/', 'edit_place_view', name="place_edit"),

    url(r'^places/delete/(?P<place_id>\d+)/', 'delete_place_view', name="place_delete"),

    url(r'^author/new/', 'create_author_view', name="create_author"),

    url(r'^author/edit/(?P<author_id>\d+)/', 'edit_author_view', name="edit_author"),

    url(r'^book/new/', 'create_book_view', name="create_book"),

    url(r'^book/edit/(?P<book_id>\d+)/', 'edit_book_view', name="edit_book"),
)
