from django.contrib import admin
from MovieApp.models import Genre, Movie, SubGenre, Actor, Director

# Register your models here.

admin.site.register(Genre),
admin.site.register(Movie),
admin.site.register(SubGenre),
admin.site.register(Actor),
admin.site.register(Director),