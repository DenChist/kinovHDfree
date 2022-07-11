from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(null=False)
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=500)
    year = models.IntegerField(null=False)
    country = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    age_rating = models.CharField(max_length=16)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='movie')
    torrent = models.FileField(upload_to='torrent', null=True)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name
