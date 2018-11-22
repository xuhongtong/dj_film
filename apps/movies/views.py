from django.shortcuts import render

# Create your views here.
from apps.movies.models import TFilm


def index(request):
    films = TFilm.objects.filter(cata_log_name='电影').order_by('-update_time')[0:12]
    fi= TFilm.objects.filter(cata_log_name='电影').order_by('-update_time')[0:10]
    return render(request, 'index.html', context={'films': films, 'fi': fi})


def detail(request, id):
    films = TFilm.objects.filter(id=id)
    return render(request, 'index.html', context={'films': films})
