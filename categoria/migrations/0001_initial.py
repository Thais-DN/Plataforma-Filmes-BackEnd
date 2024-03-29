# Generated by Django 5.0.1 on 2024-01-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='movie_images/')),
                ('filmes', models.ManyToManyField(to='movie.filme')),
            ],
        ),
    ]
