from django.contrib import admin
from movies.models import Movie, Director, Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year")
    search_fields = ["title", "directed_by__name"]
    list_filter = ("directed_by", )

class DirectorAdmin(admin.ModelAdmin):
    pass

class ActorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
