from django.contrib import admin
from MovieApp.models import Genre, Movie, SubGenre

# Register your models here.

admin.site.register(Genre),
admin.site.register(Movie),
admin.site.register(SubGenre),