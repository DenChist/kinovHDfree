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
    metadata = bencodepy.decode_from_file(movie.torrent.path)
    subj = metadata[b'info']
    hashcontents = bencodepy.encode(subj)
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest).decode()
    magnet = 'magnet:?'\
             + 'xt=urn:btih:' + b32hash\
             + '&dn=' + metadata[b'info'][b'name'].decode()\
             + '&tr=' + metadata[b'announce'].decode() + '&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com'\
             + '&xl=' + str(metadata[b'info'][b'length'])
    return render(request, 'season.html', {'movie': movie, 'magnet': magnet})
