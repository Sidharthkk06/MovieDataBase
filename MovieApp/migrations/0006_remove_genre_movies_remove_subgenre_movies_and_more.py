# Generated by Django 4.2.7 on 2024-04-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0005_movie_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='subgenre',
            name='movies',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='MovieApp.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='subgenres',
            field=models.ManyToManyField(related_name='movies', to='MovieApp.subgenre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('G', 'G - General Audiences'), ('PG', 'PG - Parental Guidance Suggested'), ('PG-13', 'PG-13 - Parents Strongly Cautioned'), ('R', 'R - Restricted'), ('NC-17', 'NC-17 - Adults Only'), ('Unrated', 'Unrated')], default='Unrated', max_length=10),
        ),
        migrations.RemoveField(
            model_name='subgenre',
            name='parent_genre',
        ),
        migrations.AddField(
            model_name='subgenre',
            name='parent_genre',
            field=models.ManyToManyField(related_name='subgenres', to='MovieApp.genre'),
        ),
    ]
