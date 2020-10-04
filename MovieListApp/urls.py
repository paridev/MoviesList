from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.movie_list, {'films_data_url': 'https://ghibliapi.herokuapp.com/films/',
                                      'people_data_url': 'https://ghibliapi.herokuapp.com/people/'}),
]
