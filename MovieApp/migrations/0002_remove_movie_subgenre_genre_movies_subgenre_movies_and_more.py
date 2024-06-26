# Generated by Django 4.2.7 on 2024-03-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='subgenre',
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
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
