# Generated by Django 5.0.1 on 2024-01-10 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_remove_filme_categoria_remove_filme_subcategoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.grupo'),
        ),
    ]
