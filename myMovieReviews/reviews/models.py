from django.db import models

# Create your models here.
RATING_CHOICES = [
    (x / 2, f'{x/2} 점') for x in range(2, 11)
]

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
    rating = models.FloatField(choices=RATING_CHOICES)
    running_time = models.IntegerField(help_text="단위: 분")
    content = models.TextField()