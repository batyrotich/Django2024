
from django.conf.urls import url, include
from watchlist_app.views import movie_list, movie_details



urlpatterns = [
    url('list/', movie_list, name='movie_list'),
    url('<int:pk>', movie_details, name='movie-detail'),
]