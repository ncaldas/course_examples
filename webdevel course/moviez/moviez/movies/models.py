from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    notes = models.TextField(blank=True, null=True)
    directed_by = models.ForeignKey('Director')
    starring = models.ManyToManyField('Actor')
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

#another type of model that will take into consideration that the movie can be directed and starring the same person
#class Person(models.Models):
#   name = models.CharField(max_length=100)

#class Movie)model.sModel):
#   title: models.CharField(max_length=100)
#   actor = models.ManyToMany("Person", related_name="directed_movies")
#   director = models.ForeignKey("Person", related_name="directed_movies")

