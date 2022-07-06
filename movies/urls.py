from django.urls import path
from .views import index_page, player_page


urlpatterns = [
    path('', index_page),
    path('movie/<int:movie_id>', player_page)
]
