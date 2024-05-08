from django.db import models

# Create your models here.
    
class Genre(models.Model):
    genre_name = models.CharField(max_length=200)
    description = models.TextField()
    movies = models.ManyToManyField('Movie', related_name='genres')

    def __str__(self):
        return self.genre_name
    

class SubGenre(models.Model):
    subgenre_name = models.CharField(max_length=200)
    description = models.TextField()
    parent_genre = models.ForeignKey(Genre, on_delete = models.CASCADE, null=True)
    movies = models.ManyToManyField('Movie', related_name='subgenres')

    def __str__(self):
        return self.subgenre_name
    

class Actor(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name
    

class Director(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    MPAA_RATING_CHOICES = [
        ('G', 'G - General Audiences'),
        ('PG', 'PG - Parental Guidance Suggested'),
        ('PG-13', 'PG-13 - Parents Strongly Cautioned'),
        ('R', 'R - Restricted'),
        ('NC-17', 'NC-17 - Adults Only'),
        ('Unrated', 'Unrated'),
]

    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/',null=True)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')
    language = models.CharField(max_length=100)
    duration = models.CharField(max_length = 30)
    Summary = models.TextField()
    youtube_video_id = models.CharField(max_length=50, blank=True, null=True)
    rating = models.CharField(max_length=10, choices=MPAA_RATING_CHOICES, default='Unrated')

    def __str__(self):
        return self.title

