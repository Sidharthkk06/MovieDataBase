# Generated by Django 4.2.7 on 2024-05-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0009_userreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.AddField(
            model_name='userreview',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
    ]
