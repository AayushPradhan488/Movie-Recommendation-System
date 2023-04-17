from django.http import HttpResponse
from django.template import loader
from .models import Movie

def main(request):
    movie=Movie.objects.all().values()
    #print(movie)
    template = loader.get_template('main.html')
    context = {
        'movie': movie,
    }
    return HttpResponse(template.render(context,request))