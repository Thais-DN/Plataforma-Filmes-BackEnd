# Generated by Django 5.0.1 on 2024-01-10 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_subcategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='filmes',
        ),
        migrations.RemoveField(
            model_name='subcategoria',
            name='filmes',
        ),
    ]
