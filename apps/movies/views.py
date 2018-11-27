from django.shortcuts import render

# Create your views here.
from apps.movies.models import TFilm


def index(request):
    film_movies1 = TFilm.objects.filter(cata_log_name='电影').order_by('-update_time')[0:12]
    film_movies2= TFilm.objects.filter(cata_log_name='电影').order_by('-update_time')[0:10]
    film_teleplays1 = TFilm.objects.filter(cata_log_name='电视剧').order_by('-update_time')[0:12]
    film_teleplays2 = TFilm.objects.filter(cata_log_name='电视剧').order_by('-update_time')[0:10]
    film_animations1 = TFilm.objects.filter(cata_log_name='动漫').order_by('-update_time')[0:12]
    film_animations2 = TFilm.objects.filter(cata_log_name='动漫').order_by('-update_time')[0:10]
    context = {'film_movies1': film_movies1,
               'film_movies2': film_movies2,
               'film_teleplays1': film_teleplays1,
               'film_teleplays2': film_teleplays2,
               'film_animations1': film_animations1,
               'film_animations2': film_animations2}
    return render(request, 'index.html', context)


def detail(request, id):
    films = TFilm.objects.get(id=id)
    return render(request, 'detail.html', context={'films': films})
