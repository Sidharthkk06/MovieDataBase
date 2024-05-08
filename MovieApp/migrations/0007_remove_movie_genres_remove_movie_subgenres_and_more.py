# Generated by Django 4.2.7 on 2024-04-01 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0006_remove_genre_movies_remove_subgenre_movies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='subgenres',
        ),
        migrations.AddField(
            model_name='genre',
            name='movies',
            field=models.ManyToManyField(related_name='genres', to='MovieApp.movie'),
        ),
        migrations.AddField(
            model_name='subgenre',
            name='movies',
            field=models.ManyToManyField(related_name='subgenres', to='MovieApp.movie'),
        ),
        migrations.RemoveField(
            model_name='subgenre',
            name='parent_genre',
        ),
        migrations.AddField(
            model_name='subgenre',
            name='parent_genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MovieApp.genre'),
        ),
    ]