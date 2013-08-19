from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)#char field used but only allows 255 characters but txtfield would be more than 255 characters, but search would not be as quick
    notes = models.TextField()
    birth_place = models.ForeignKey('Place')

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.SmallIntegerField()
    author = models.ForeignKey('Author') #refers to the author who wrote the book, and the 'Author' has to be in quotes so that when the models.ForeignKey searches everywhere

    def __unicode__(self):
        return u"'{0}' written in {1} by {2}".format(self.title, self.published_year, self.author)

class Place(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return u"{0} ({1}, {2})".format(self.name,self.latitude,
                                        self.longitude)#by default django will paint on the terminal just the object and where it is coming from, but this will tell python how to show the data, .format shows it
    
