from django.shortcuts import render
from .models import Movie
import bencodepy
import hashlib
import base64

def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'main.html', {'movies': movies})


def player_page(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)

    magnet = ""
    return render(request, 'season.html', {'movie': movie, 'magnet': magnet})
