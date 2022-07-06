from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(null=False)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='movie')
    torrent_id = models.CharField(max_length=4096)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name
