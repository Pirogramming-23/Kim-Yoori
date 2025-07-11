from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    rating = models.IntegerField()
    running_time = models.IntegerField(help_text="단위: 분")
    content = models.TextField()