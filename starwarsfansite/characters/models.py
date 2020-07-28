from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=50)
    terrain = models.CharField(max_length=100)
    population = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField()
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=200)
    planets = models.ManyToManyField(
        Planet,
        related_name='movies',
    )

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=20)
    genre = models.CharField(max_length=10)
    movies = models.ManyToManyField(
        Movie,
        related_name='characters',
    )

    def __str__(self):
        return self.name
