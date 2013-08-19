from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from movies.forms import MovieForm, DirectorForm, ActorForm
from movies.models import Movie, Director, Actor

def home(request):
    return render_to_response("moviez/home.html", RequestContext(request, {
    'obj_list': [1,2,3,4],
    }))

def movies_view(request):
    movies_list = Movie.objects.all()
    return render_to_response("movies.html", RequestContext(request,{
    "movies_list": movies_list,
    "is_info": False
    }))


def movies_info_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movies_list = Movie.objects.all()
    actor_list = movie.starring.all()
    director = movie.directed_by
    return render_to_response("movies.html", RequestContext(request, {
    "actor_list": actor_list,
    "director": director,
    "movies_list": movies_list,
    "is_info": True
    }))
