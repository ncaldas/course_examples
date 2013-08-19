from django import forms
from movies.models import Movie, Director, Actor

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie

class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director

class ActorForm(forms.ModelForm):

    class Meta:
        model = Actor
